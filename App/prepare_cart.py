from App.utils import session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def product_in_cart(url_to_post, product_id, gtm4wp_product_data):
    url = url_to_post
    data = {
        "quantity": 1,
        "add-to-cart": product_id,
        "gtm4wp_product_data": gtm4wp_product_data
    }
    session = session_manager.get_session()
    #######################################################
    for i in range(1):
        ################################################# more than 1 if simulate buy multiple same product
        response = session.post(url, data=data)
        print("Statut:", response.status_code)
        if response.status_code == 504:
            return None
        # print("Contenu:", response.text)
        print("Cookies reçus :")
        for cookie in session.cookies:
            print("session | ", cookie.name, "=", cookie.value)
            cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain = cookie.domain, path= cookie.path)

    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    number_products_in_cart = soup.find("span", class_="elementor-button-icon-qty").get("data-counter")
    print("number products in cart:", number_products_in_cart)

    price_in_cart = soup.find("span", class_="elementor-button-text")
    price_in_cart = price_in_cart.find("span", class_="woocommerce-Price-amount amount")
    price_in_cart = price_in_cart.find("bdi").find(text=True, recursive=False).strip()
    print("price in cart:", price_in_cart)

    price_one_product = soup.find("p", class_="price")
    price_one_product = price_one_product.find("span", class_="woocommerce-Price-amount amount")
    price_one_product = price_one_product.find("bdi").find(text=True, recursive=False).strip()
    print("price to one product:", price_one_product)

    if number_products_in_cart == "1" and price_in_cart == price_one_product:
        print("Success one product in cart")
        return 200
    elif int(number_products_in_cart) > 1:
        print("TO MANY PRODUCTS IN CART. There is", number_products_in_cart, "products.")
    elif price_in_cart != price_one_product:
        print("PRICE IN CART IS NOT PRICE FOR EXPECTED PRODUCT")
    else:
        print("BAD HTML PARSING")
    print("Need to restart program")
    return "restart"


def check_order_validation(price_one_product):
    url = "https://www.cardshunter.fr/commander/"
    session = session_manager.get_session()
    response = session.get(url)
    print("Statut:", response.status_code)
    # print(response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
        cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain = cookie.domain, path= cookie.path)

    soup = BeautifulSoup(response.text, "html.parser")
    number_products_in_cart = soup.find("td", class_="product-name")
    if number_products_in_cart == None:
        print("CART IS EMPTY")
        return 200
    number_products_in_cart = number_products_in_cart.find("strong", class_="product-quantity").get_text()
    number_products_in_cart = number_products_in_cart.split()[-1]
    print("number products in cart:", number_products_in_cart)

    subtotal_price = soup.find("tr", class_="cart-subtotal").find("bdi").find(text=True, recursive=False).strip()
    print("price in cart:", subtotal_price)
    print("price to one product:", price_one_product)

    if number_products_in_cart == "1" and subtotal_price == price_one_product:
        print("Success one product in cart")
        return 200
    elif int(number_products_in_cart) > 1:
        print("TO MANY PRODUCTS IN CART. There is", number_products_in_cart, "products.")
    elif subtotal_price != price_one_product:
        print("PRICE IN CART IS NOT PRICE FOR EXPECTED PRODUCT")
    else:
        print("BAD HTML PARSING")
    print("Need to restart program")
    return "restart"
