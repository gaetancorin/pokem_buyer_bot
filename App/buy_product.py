import session_manager as session_manager
import configparser
from bs4 import BeautifulSoup
from pathlib import Path

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def prepare_to_cart(write_html= False):
    session = session_manager.get_session()
    response = session.get(url_product_card)

    soup = BeautifulSoup(response.text, "html.parser")
    shortlink = soup.find('link', {'rel': 'shortlink'})['href']
    product_id = shortlink.split('p=')[1]
    form = soup.find('form', {'action': url_product_card})
    if form:
        print("button ok, status code:", response.status_code)
        # print(form)
        url_to_post = form['action']
        gtm4wp_input = form.find('input', {'name': 'gtm4wp_product_data'})
        gtm4wp_product_data = gtm4wp_input['value']
        print("product_id = ", product_id)
        print("url_to_post = ", url_to_post)
        print("gtm4wp_product_data = ", gtm4wp_product_data)
        return url_to_post, product_id, gtm4wp_product_data
    else:
        print("BUTTON NOT FOUND, STATUS CODE: ", response.status_code)
        # écrire le code html recu si bouton pas trouvé
        if write_html == True:
            Path("../outpout/").mkdir(parents=True, exist_ok=True)
            with open("../outpout/outpout_prepare_to_cart_fail.html", "w", encoding="utf-8") as f:
                f.write(response.text)
        return None


def product_in_cart(url_to_post, product_id, gtm4wp_product_data):
    url = url_to_post
    data = {
        "quantity": 1,
        "add-to-cart": product_id,
        "gtm4wp_product_data": gtm4wp_product_data
    }
    session = session_manager.get_session()
    response = session.post(url, data=data)

    # Afficher le contenu de la réponse
    print("Statut:", response.status_code)
    if response.status_code == 504:
        return None
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)



    #################################""" 2
    response = session.post(url, data=data)
    # Afficher le contenu de la réponse
    print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
    # ################################""" 3
    # response = session.post(url, data=data)
    # # Afficher le contenu de la réponse
    # print("Statut:", response.status_code)
    # # print("Contenu:", response.text)
    # print("Cookies reçus :")
    # for cookie in session.cookies:
    #     print("session | ", cookie.name, "=", cookie.value)
    # ################################""" 4
    # response = session.post(url, data=data)
    # # Afficher le contenu de la réponse
    # print("Statut:", response.status_code)
    # # print("Contenu:", response.text)
    # print("Cookies reçus :")
    # for cookie in session.cookies:
    #     print("session | ", cookie.name, "=", cookie.value)




    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    number_products_in_cart = soup.find("span", class_="elementor-button-icon-qty").get("data-counter")
    print("number products in cart:", number_products_in_cart)

    price_in_cart = soup.find("span", class_="elementor-button-text")
    price_in_cart = price_in_cart.find("span", class_="woocommerce-Price-amount amount")
    price_in_cart = price_in_cart.find("bdi").find(text=True, recursive=False).strip()
    print("price in cart:", price_in_cart)

    price_to_one_product = soup.find("p", class_="price")
    price_to_one_product = price_to_one_product.find("span", class_="woocommerce-Price-amount amount")
    price_to_one_product = price_to_one_product.find("bdi").find(text=True, recursive=False).strip()
    print("price to one product:", price_to_one_product)

    if number_products_in_cart == "1" and price_in_cart == price_to_one_product:
        print("Success one product in cart")
        return 200
    elif int(number_products_in_cart) > 1:
        print("TO MANY PRODUCTS IN CART. There is", number_products_in_cart, "products.")
    elif price_in_cart != price_to_one_product:
        print("PRICE IN CART IS NOT PRICE FOR EXPECTED PRODUCT")
    print("Need to restart program")
    # return "restart"


def verify_product_in_cart():
    session = session_manager.get_session()
    response = session.get(url_product_card)
    print("Statut:", response.status_code)
    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    number_products_in_cart = soup.find("span", class_="elementor-button-icon-qty").get("data-counter")
    print("number products in cart:", number_products_in_cart)

    price_in_cart = soup.find("span", class_="elementor-button-text")
    price_in_cart = price_in_cart.find("span", class_="woocommerce-Price-amount amount")
    price_in_cart = price_in_cart.find("bdi").find(text=True, recursive=False).strip()
    print("price in cart:", price_in_cart)

    price_to_one_product = soup.find("p", class_="price")
    price_to_one_product = price_to_one_product.find("span", class_="woocommerce-Price-amount amount")
    price_to_one_product = price_to_one_product.find("bdi").find(text=True, recursive=False).strip()
    print("price to one product:", price_to_one_product)

    if number_products_in_cart == "1" and price_in_cart == price_to_one_product:
        print("Success one product in cart")
        return 200
    elif int(number_products_in_cart) > 1:
        print("TO MANY PRODUCTS IN CART. There is", number_products_in_cart, "products.")
    elif price_in_cart != price_to_one_product:
        print("PRICE IN CART IS NOT PRICE FOR EXPECTED PRODUCT")
    print("Need to restart program")
    Path("../outpout/").mkdir(parents=True, exist_ok=True)
    with open("../outpout/outpout_fail_verify_product.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    return "restart"



# def check_order_validation():
#     url = "https://www.cardshunter.fr/commander/"
#     session = session_manager.get_session()
#     response = session.get(url)
#     print("Statut:", response.status_code)
#     print(response.text)
