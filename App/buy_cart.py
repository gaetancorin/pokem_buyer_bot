import App.utils.cookies_manager as cookies_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
PRENOM = config['VARIABLEFORM']['PRENOM']
NOM = config['VARIABLEFORM']['NOM']
PAYS = config['VARIABLEFORM']['PAYS']
ADRESSE_NUMERO_NOM_RUE = config['VARIABLEFORM']['ADRESSE_NUMERO_NOM_RUE']
ADRESSE_BATIMENT_APPARTEMENT = config['VARIABLEFORM']['ADRESSE_BATIMENT_APPARTEMENT']
CODE_POSTAL = config['VARIABLEFORM']['CODE_POSTAL']
VILLE = config['VARIABLEFORM']['VILLE']
TELEPHONE = config['VARIABLEFORM']['TELEPHONE']
EMAIL = config['VARIABLEFORM']['EMAIL']
NOM_PROPRIETAIRE_CARTE_BLEU = config['VARIABLEFORM']['NOM_PROPRIETAIRE_CARTE_BLEU']
NUMERO_CARTE_BLEU = config['VARIABLEFORM']['NUMERO_CARTE_BLEU']
DATE_EXPIRATION_CARTE_BLEU = config['VARIABLEFORM']['DATE_EXPIRATION_CARTE_BLEU'].replace("/", "").replace("_", "").replace("-", "")
NUMERO_SECURITE_CARTE_BLEU = config['VARIABLEFORM']['NUMERO_SECURITE_CARTE_BLEU']

def place_order_by_selenium():
    # Initialise solanium driver cookies with good url
    driver = webdriver.Chrome()
    driver.get("https://www.cardshunter.fr/wp-content/smush-webp/2021/12/cropped-Logo_fond_blanc_e7e3f730-4a44-48a0-be6e-e087faab7c51_540x-300x163.png.webp")

    # Fill cookies from session_manager to solanium
    for key, value in cookies_manager.get_cookies().items():
        selenium_cookie =  {
            'name': key,
            'value': value["value"],
            'domain': value["domain"],
            'path': value["path"],
        }
        driver.add_cookie(selenium_cookie)

    # Get purchase page, fill inputs and shop !
    driver.get("https://www.cardshunter.fr/commander/")

    print("fill billing_first_name")
    billing_first_name = driver.find_element(By.ID, "billing_first_name")
    billing_first_name.clear()
    billing_first_name.send_keys(PRENOM)

    print("fill billing_last_name")
    billing_last_name = driver.find_element(By.ID, "billing_last_name")
    billing_last_name.clear()
    billing_last_name.send_keys(NOM)

    print("fill billing_country_element (FR)")
    billing_country_element = driver.find_element(By.ID, "billing_country")
    billing_country_selector = Select(billing_country_element)
    billing_country_selector.select_by_value(PAYS)

    print("fill billing_address_1")
    billing_address_1 = driver.find_element(By.ID, "billing_address_1")
    billing_address_1.clear()
    billing_address_1.send_keys(ADRESSE_NUMERO_NOM_RUE)

    print("fill billing_address_2")
    billing_address_2 = driver.find_element(By.ID, "billing_address_2")
    billing_address_2.clear()
    billing_address_2.send_keys(ADRESSE_BATIMENT_APPARTEMENT)

    print("fill billing_postcode")
    billing_postcode = driver.find_element(By.ID, "billing_postcode")
    billing_postcode.clear()
    billing_postcode.send_keys(CODE_POSTAL)

    print("fill billing_city")
    billing_city = driver.find_element(By.ID, "billing_city")
    billing_city.clear()
    billing_city.send_keys(VILLE)

    print("fill billing_phone")
    billing_phone = driver.find_element(By.ID, "billing_phone")
    billing_phone.clear()
    billing_phone.send_keys(TELEPHONE)

    print("fill billing_email")
    billing_email = driver.find_element(By.ID, "billing_email")
    billing_email.clear()
    billing_email.send_keys(EMAIL)

    print("fill shipping_first_name")
    shipping_first_name = driver.find_element(By.ID, "shipping_first_name")
    shipping_first_name.clear()
    shipping_first_name.send_keys(PRENOM)

    print("fill shipping_last_name")
    shipping_last_name = driver.find_element(By.ID, "shipping_last_name")
    shipping_last_name.clear()
    shipping_last_name.send_keys(NOM)

    print("fill shipping_country_element (FR)")
    shipping_country_element = driver.find_element(By.ID, "shipping_country")
    shipping_country_selector = Select(shipping_country_element)
    shipping_country_selector.select_by_value(PAYS)

    print("fill shipping_address_1")
    shipping_address_1 = driver.find_element(By.ID, "shipping_address_1")
    shipping_address_1.clear()
    shipping_address_1.send_keys(ADRESSE_NUMERO_NOM_RUE)

    print("fill shipping_address_2")
    shipping_address_2 = driver.find_element(By.ID, "shipping_address_2")
    shipping_address_2.clear()
    shipping_address_2.send_keys(ADRESSE_BATIMENT_APPARTEMENT)

    print("fill shipping_postcode")
    shipping_postcode = driver.find_element(By.ID, "shipping_postcode")
    shipping_postcode.clear()
    shipping_postcode.send_keys(CODE_POSTAL)

    print("fill shipping_city")
    shipping_city = driver.find_element(By.ID, "shipping_city")
    shipping_city.clear()
    shipping_city.send_keys(VILLE)

    print("fill shipping_phone")
    shipping_phone = driver.find_element(By.ID, "shipping_phone")
    shipping_phone.clear()
    shipping_phone.send_keys(TELEPHONE)

    # COLIS AVEC SIGNATURE: "shipping_method_0_lpc_sign58"
    # COLIS SANS SIGNATURE: "shipping_method_0_lpc_nosign1"
    # COLIS LETTRE SUIVI: "shipping_method_0_fish_n_ships35"
    # COLIS POINT RETRAIT: "shipping_method_0_lpc_relay59"
    # (le point retrait doit être préenregistrer)

    # print("click shipping method")
    # # AVEC SIGNATURE
    # radio_button = driver.find_element(By.ID, "shipping_method_0_lpc_sign58")
    # driver.execute_script("arguments[0].click();", radio_button)
    #
    print("fill sans signature")
    # SANS SIGNATURE
    radio_button = driver.find_element(By.ID, "shipping_method_0_lpc_nosign1")
    driver.execute_script("arguments[0].click();", radio_button)

    # print("fill point retrait")
    # # POINT RETRAIT
    # radio_button = driver.find_element(By.ID, "shipping_method_0_lpc_relay59")
    # driver.execute_script("arguments[0].click();", radio_button)

    # print("fill lettre suivi")
    # # LETTRE SUIVI
    # radio_button = driver.find_element(By.ID, "shipping_method_0_fish_n_ships35")
    # driver.execute_script("arguments[0].click();", radio_button)

    # go inside to frame for credit card holder name
    iframe = driver.find_element(By.ID, "cardholder")
    driver.switch_to.frame(iframe)
    credit_card_holder_name = driver.find_element(By.ID, "cardholder")
    credit_card_holder_name.clear()
    credit_card_holder_name.send_keys(NOM_PROPRIETAIRE_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()


    # go inside to frame for credit card number
    iframe = driver.find_element(By.ID, "pan")
    driver.switch_to.frame(iframe)
    credit_card_number = driver.find_element(By.ID, "credit-card-number")
    credit_card_number.clear()
    credit_card_number.send_keys(NUMERO_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    # go inside to frame for credit card expiration
    iframe = driver.find_element(By.ID, "exp")
    driver.switch_to.frame(iframe)
    credit_card_exp = driver.find_element(By.ID, "expiration")
    credit_card_exp.clear()
    credit_card_exp.send_keys(DATE_EXPIRATION_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    # go inside to frame for credit card secure number
    iframe = driver.find_element(By.ID, "cvv")
    driver.switch_to.frame(iframe)
    credit_card_secure_number = driver.find_element(By.ID, "cvv")
    credit_card_secure_number.clear()
    credit_card_secure_number.send_keys(NUMERO_SECURITE_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()





    print("ok")


