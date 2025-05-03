from App.utils import session_manager as session_manager
import configparser
from bs4 import BeautifulSoup
from pathlib import Path

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def place_order(price_one_product):
    url = "https://www.cardshunter.fr/commander/"
    session = session_manager.get_session()
    response = session.get(url)
    print("Statut:", response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    number_products_in_cart = soup.find("td", class_="product-name").find("strong", class_="product-quantity").get_text()
    number_products_in_cart = number_products_in_cart.split()[-1]
    print("number products in cart:", number_products_in_cart)

    subtotal_price = soup.find("tr", class_="cart-subtotal").find("bdi").find(text=True, recursive=False).strip()
    print("price in cart:", subtotal_price)
    print("price to one product:", price_one_product)

    if number_products_in_cart == "1" and subtotal_price == price_one_product:
        print("Success one product in cart")
        Path("../outpout/").mkdir(parents=True, exist_ok=True)
        with open("../outpout/buy_cart_get.html", "w", encoding="utf-8") as f:
            f.write(response.text)