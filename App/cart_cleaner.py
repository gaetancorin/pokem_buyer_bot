import App.utils.session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
from bs4 import BeautifulSoup
from pathlib import Path

def clean_cart_if_product():
    url = "https://www.cardshunter.fr/panier/"
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(url)
        print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
        cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain=cookie.domain, path=cookie.path)
    Path("../outpout/").mkdir(parents=True, exist_ok=True)
    with open("../outpout/cart_content.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    cart_empty = soup.find("div", class_="cart-empty")
    if cart_empty:
        print("No product in Cart")
    else:
        print("Product in Cart")
        link_to_delete_product = soup.find("td", class_="product-remove").find("a")["href"]
        print("link_to_delete_product", link_to_delete_product)
        clean_cart(link_to_delete_product)

def clean_cart(link_to_clean_cart):
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(link_to_clean_cart)
        print("Statut:", response.status_code)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
        cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain=cookie.domain, path=cookie.path)
    soup = BeautifulSoup(response.text, "html.parser")
    cart_empty = soup.find("div", class_="cart-empty")
    if cart_empty:
        print("Cart is now Clean")
