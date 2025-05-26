import App.utils.session_manager as session_manager
import App.dev_utils.cookies_manager as cookies_manager
import App.utils.config_file_manager as config_file_manager
from bs4 import BeautifulSoup

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
    config_file = config_file_manager.get_config_file()
    username = config_file['VARIABLEENV']['USERNAME']
    password = config_file['VARIABLEENV']['PASSWORD']

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
        return "Done"
    else:
        print("Connection Failed")
        return None




if __name__ == "__main__":
    config_file_manager.set_config_file_on_debug_mode(1)
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = get_proof_of_connection()
    print("---- GET COOKIES ----")
    ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    connect_by_cookies()
    print("---- END -----")