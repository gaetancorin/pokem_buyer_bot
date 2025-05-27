import App.utils.session_manager as session_manager
import App.dev_utils.cookies_manager as cookies_manager
import App.dev_utils.file_saver as file_saver
from bs4 import BeautifulSoup

def clean_cart_if_product():
    url = "https://www.cards(do_not_mention)hunter.fr/panier/".replace("(do_not_mention)", "")
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(url)
        print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    cookies_manager.displayed_cookies_if_activated(session)
    file_saver.save_html_file_for_futur_analysis(file_name="cart_content", response=response)

    soup = BeautifulSoup(response.text, "html.parser")
    cart_empty = soup.find("div", class_="cart-empty")
    if cart_empty:
        print("No product in Cart")
    else:
        print("Found product in Cart")
        link_to_delete_product = soup.find("td", class_="product-remove").find("a")["href"]
        print("link_to_delete_product", link_to_delete_product)
        clean_cart(link_to_delete_product)

def clean_cart(link_to_clean_cart):
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(link_to_clean_cart)
        print("Statut:", response.status_code)
    cookies_manager.displayed_cookies_if_activated(session)
    soup = BeautifulSoup(response.text, "html.parser")
    cart_empty = soup.find("div", class_="cart-empty")
    if cart_empty:
        print("Cart is now Clean")
