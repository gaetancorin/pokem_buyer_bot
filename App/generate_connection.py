import App.utils.session_manager as session_manager
import App.dev_utils.cookies_manager as cookies_manager
import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('../config/config.ini')
username = config['VARIABLEENV']['USERNAME']
password = config['VARIABLEENV']['PASSWORD']


def get_proof_of_connection():
    url = "https://www.cardshunter.fr/mon-compte/"
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
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
    response = None
    while not response or response.status_code != 200:
        response = session.post(url, data=data)
        print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    cookies_manager.displayed_cookies_if_activated(session)

def connect_by_cookies():
    url = "https://www.cardshunter.fr/mon-compte/"
    session = session_manager.get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(url)
        print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    cookies_manager.displayed_cookies_if_activated(session)
    soup = BeautifulSoup(response.text, 'html.parser')
    if "Bonjour" in soup.get_text() and "Déconnexion" in soup.get_text():
        print("Connection Success")
    else:
        print("Connection Failed")




if __name__ == "__main__":
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = get_proof_of_connection()
    print("---- GET COOKIES ----")
    ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    connect_by_cookies()
    print("---- END -----")