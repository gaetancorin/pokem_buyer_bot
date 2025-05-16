from App.utils import session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
import configparser
from bs4 import BeautifulSoup

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def add_product_in_cart(url_to_post, product_id, gtm4wp_product_data):
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

    return response.status_code, response.text
