import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
username = config['VARIABLEENV']['USERNAME']
password = config['VARIABLEENV']['PASSWORD']

session = requests.Session()

def scrapping_post():

    url = "https://www.cardshunter.fr/mon-compte/"

    # Données du formulaire à envoyer
    data = {
        "username": username,
        "password": password,
        "woocommerce-login-nonce": "ff5151aa61",
        "_wp_http_referer": "/mon-compte/",
        "login": "Se connecter"
    }

    # Faire la requête POST
    response = session.post(url, data=data)

    # Afficher le contenu de la réponse
    print("Statut:", response.status_code)
    # print("Contenu:", response.text)
    print("Cookies reçus :")
    print(response.cookies)
    for cookie in response.cookies:
        print("response | ", cookie.name, "=", cookie.value)

    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)

def scrapping_get():
    url = "https://www.cardshunter.fr/mon-compte/"

    # Faire la requête POST
    response = session.get(url)

    # Afficher le contenu de la réponse
    print("Statut:", response.status_code)
    print("Contenu:", response.text)


if __name__ == "__main__":
    print("----TEST POST----")
    scrapping_post()
    print("----TEST GET----")
    scrapping_get()
    print("----END-----")