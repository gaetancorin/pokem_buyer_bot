import App.utils.cookies_manager as cookies_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
NUMERO_CARTE_BLEU = config['VARIABLEFORM']['NUMERO_CARTE_BLEU']
PRENOM = config['VARIABLEFORM']['PRENOM']
NOM = config['VARIABLEFORM']['NOM']
PAYS = config['VARIABLEFORM']['PAYS']
ADRESSE_NUMERO_NOM_RUE = config['VARIABLEFORM']['ADRESSE_NUMERO_NOM_RUE']
ADRESSE_BATIMENT_APPARTEMENT = config['VARIABLEFORM']['ADRESSE_BATIMENT_APPARTEMENT']
CODE_POSTAL = config['VARIABLEFORM']['CODE_POSTAL']
VILLE = config['VARIABLEFORM']['VILLE']
TELEPHONE = config['VARIABLEFORM']['TELEPHONE']
EMAIL = config['VARIABLEFORM']['EMAIL']

def selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.cardshunter.fr/wp-content/smush-webp/2021/12/cropped-Logo_fond_blanc_e7e3f730-4a44-48a0-be6e-e087faab7c51_540x-300x163.png.webp")
    for key, value in cookies_manager.get_cookies().items():
        selenium_cookie =  {
            'name': key,
            'value': value["value"],
            'domain': value["domain"],
            'path': value["path"],
        }
        driver.add_cookie(selenium_cookie)
    driver.get("https://www.cardshunter.fr/commander/")

    first_name_input = driver.find_element(By.ID, "billing_first_name")
    first_name_input.clear()
    first_name_input.send_keys(PRENOM)

    last_name_input = driver.find_element(By.ID, "billing_last_name")
    last_name_input.clear()
    last_name_input.send_keys(NOM)

    country_element = driver.find_element(By.ID, "billing_country")
    country_selector = Select(country_element)
    country_selector.select_by_value(PAYS)

    billing_address_1 = driver.find_element(By.ID, "billing_address_1")
    billing_address_1.clear()
    billing_address_1.send_keys(ADRESSE_NUMERO_NOM_RUE)

    billing_address_2 = driver.find_element(By.ID, "billing_address_2")
    billing_address_2.clear()
    billing_address_2.send_keys(ADRESSE_BATIMENT_APPARTEMENT)

    billing_postcode = driver.find_element(By.ID, "billing_postcode")
    billing_postcode.clear()
    billing_postcode.send_keys(CODE_POSTAL)

    billing_city = driver.find_element(By.ID, "billing_city")
    billing_city.clear()
    billing_city.send_keys(VILLE)

    billing_phone = driver.find_element(By.ID, "billing_phone")
    billing_phone.clear()
    billing_phone.send_keys(TELEPHONE)

    billing_email = driver.find_element(By.ID, "billing_email")
    billing_email.clear()
    billing_email.send_keys(TELEPHONE)





    print("ok")


# HELP FOR CREDIT CARD
#     # go inside to frame to credit card
#     iframe = driver.find_element(By.ID, "pan")
#     driver.switch_to.frame(iframe)
#
#     credit_card_number = driver.find_element(By.ID, "credit-card-number")
#     credit_card_number.clear()
#     credit_card_number.send_keys(NUMERO_CARTE_BLEU)
#
#     # get out of frame
#     driver.switch_to.default_content()
