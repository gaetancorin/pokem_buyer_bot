from App.utils import session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def check_cookies():
    # url = "https://www.cardshunter.fr/commander/"

    session = session_manager.get_session()
    print("CHECK ALL COOKIES")
    for cookie in session.cookies:
        print("session | ", cookie.name, "=", cookie.value)

    print(cookies_manager.get_cookies())
    for key, value in cookies_manager.get_cookies().items():
        print("cks_manager | ", key, "=", value)

