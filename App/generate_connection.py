import App.utils.session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
import configparser
from bs4 import BeautifulSoup
from pathlib import Path

config = configparser.ConfigParser()
config.read('../config/config.ini')
username = config['VARIABLEENV']['USERNAME']
password = config['VARIABLEENV']['PASSWORD']


def get_proof_of_connection():
    url = "https://www.cardshunter.fr/mon-compte/"
    session = session_manager.get_session()
    response = session.get(url)
    print("Statut:", response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    proof_id = soup.find('input', {'id': 'woocommerce-login-nonce'})['value']
    print("proof id = ", proof_id)
    # print(response.text)
    return proof_id


def ask_for_cookies(proof_id):
    url = "https://www.cardshunter.fr/mon-compte/"
    data = {
        "username": username,
        "password": password,
        "woocommerce-login-nonce": proof_id,
        "_wp_http_referer": "/mon-compte/",
        "login": "Se connecter"
    }
    session = session_manager.get_session()
    response = session.post(url, data=data)

    # Afficher le contenu de la réponse
    print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
        cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain = cookie.domain, path= cookie.path)

def connect_by_cookies():
    url = "https://www.cardshunter.fr/mon-compte/"
    session = session_manager.get_session()
    response = session.get(url)
    print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)
        cookies_manager.add_cookies(key=cookie.name, value=cookie.value, domain = cookie.domain, path= cookie.path)
    soup = BeautifulSoup(response.text, 'html.parser')
    if "Bonjour" in soup.get_text() and "Déconnexion" in soup.get_text():
        print("Connection Success")
    else:
        print("Connection Failed")

def clean_cart_if_product():
    url = "https://www.cardshunter.fr/panier/"
    session = session_manager.get_session()
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




if __name__ == "__main__":
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = get_proof_of_connection()
    print("---- GET COOKIES ----")
    ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    connect_by_cookies()
    print("---- CLEAN CART ----")
    clean_cart_if_product()
    print("---- END -----")