import requests
import configparser
from bs4 import BeautifulSoup

config_file = None

def set_config_file_on_debug_mode(iteration):
    global config_file
    print("USE CONFIG FILE config"+str(iteration)+".ini")
    config_file = configparser.ConfigParser()
    config_file.read("../config/config"+str(iteration)+".ini")
    return config_file

def get_session():
    global session
    if session is None:
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "fr-FR,fr;q=0.9",
            "Connection": "keep-alive"
        })
    return session

def force_new_session():
    global session
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Connection": "keep-alive"
    })
    return session

def get_proof_of_connection():
    url = "https://www.cards(do_not_mention)hunter.fr/mon-compte/".replace("(do_not_mention)", "")
    session = get_session()
    response = None
    while not response or response.status_code != 200:
        response = session.get(url)
        print("Statut:", response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    proof_id = soup.find('input', {'id': 'woocommerce-login-nonce'})['value']
    print("proof id = ", proof_id)
    # print(response.text)
    return proof_id

if __name__ == "__main__":
    set_config_file_on_debug_mode(1)
    force_new_session()
    proof_id = get_proof_of_connection()