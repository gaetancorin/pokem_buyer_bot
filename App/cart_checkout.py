import App.dev_utils.cookies_manager as cookies_manager
import App.utils.session_manager as session_manager
import App.utils.config_file_manager as config_file_manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # ou "--silent"
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

shipping_method ={}
shipping_method['1'] = "shipping_method_0_lpc_sign58" # COLIS AVEC SIGNATURE
shipping_method['2'] = "shipping_method_0_lpc_nosign1" # COLIS SANS SIGNATURE
shipping_method['3'] = "shipping_method_0_fish_n_ships35" # COLIS LETTRE SUIVI
shipping_method['4'] = "shipping_method_0_lpc_relay59" # COLIS POINT RETRAIT

def place_order_by_selenium(action):
    config_file = config_file_manager.get_config_file()
    PRENOM = config_file['VARIABLEFORM']['PRENOM']
    NOM = config_file['VARIABLEFORM']['NOM']
    PAYS = config_file['VARIABLEFORM']['PAYS']
    ADRESSE_NUMERO_NOM_RUE = config_file['VARIABLEFORM']['ADRESSE_NUMERO_NOM_RUE']
    ADRESSE_BATIMENT_APPARTEMENT = config_file['VARIABLEFORM']['ADRESSE_BATIMENT_APPARTEMENT']
    CODE_POSTAL = config_file['VARIABLEFORM']['CODE_POSTAL']
    VILLE = config_file['VARIABLEFORM']['VILLE']
    TELEPHONE = config_file['VARIABLEFORM']['TELEPHONE']
    EMAIL = config_file['VARIABLEFORM']['EMAIL']
    NOM_PROPRIETAIRE_CARTE_BLEU = config_file['VARIABLEFORM']['NOM_PROPRIETAIRE_CARTE_BLEU']
    NUMERO_CARTE_BLEU = config_file['VARIABLEFORM']['NUMERO_CARTE_BLEU']
    DATE_EXPIRATION_CARTE_BLEU = config_file['VARIABLEFORM']['DATE_EXPIRATION_CARTE_BLEU'].replace("/", "").replace("_","").replace("-", "")
    NUMERO_SECURITE_CARTE_BLEU = config_file['VARIABLEFORM']['NUMERO_SECURITE_CARTE_BLEU']
    METHODE_ENVOI = shipping_method[config_file['VARIABLEFORM']['METHODE_ENVOI']]
    NOM_ZONE_POINT_RELAIS = config_file['VARIABLEFORM']['NOM_ZONE_POINT_RELAIS']
    if action == "choose_pickup_point":
        METHODE_ENVOI = shipping_method['4']

    # Initialise solanium driver with good url for cookies
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.cardshunter.fr/wp-content/smush-webp/2021/12/cropped-Logo_fond_blanc_e7e3f730-4a44-48a0-be6e-e087faab7c51_540x-300x163.png.webp")

    # Fill cookies from session.cookies to solanium
    session = session_manager.get_session()
    cookies_manager.displayed_cookies_if_activated(session)
    for cookie in session.cookies:
        selenium_cookie = {
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
        }
        driver.add_cookie(selenium_cookie)

    # Get purchase page, fill inputs and shop !
    driver.get("https://www.cardshunter.fr/commander/")

    print("start fill billing_first_name (PRENOM)")
    billing_first_name = driver.find_element(By.ID, "billing_first_name")
    billing_first_name.clear()
    billing_first_name.send_keys(PRENOM)

    print("start fill billing_last_name (NOM)")
    billing_last_name = driver.find_element(By.ID, "billing_last_name")
    billing_last_name.clear()
    billing_last_name.send_keys(NOM)

    print("start fill billing_country_element (PAYS)")
    billing_country_element = driver.find_element(By.ID, "billing_country")
    billing_country_selector = Select(billing_country_element)
    billing_country_selector.select_by_value(PAYS)

    print("start fill billing_address_1 (ADRESSE_NUMERO_NOM_RUE)")
    billing_address_1 = driver.find_element(By.ID, "billing_address_1")
    billing_address_1.clear()
    billing_address_1.send_keys(ADRESSE_NUMERO_NOM_RUE)

    print("start fill billing_address_2 (ADRESSE_BATIMENT_APPARTEMENT)")
    billing_address_2 = driver.find_element(By.ID, "billing_address_2")
    billing_address_2.clear()
    billing_address_2.send_keys(ADRESSE_BATIMENT_APPARTEMENT)

    print("start fill billing_postcode (CODE_POSTAL)")
    billing_postcode = driver.find_element(By.ID, "billing_postcode")
    billing_postcode.clear()
    billing_postcode.send_keys(CODE_POSTAL)

    print("start fill billing_city (VILLE)")
    billing_city = driver.find_element(By.ID, "billing_city")
    billing_city.clear()
    billing_city.send_keys(VILLE)

    print("start fill billing_phone (TELEPHONE)")
    billing_phone = driver.find_element(By.ID, "billing_phone")
    billing_phone.clear()
    billing_phone.send_keys(TELEPHONE)

    print("start fill billing_email (EMAIL)")
    billing_email = driver.find_element(By.ID, "billing_email")
    billing_email.clear()
    billing_email.send_keys(EMAIL)

    print("start fill shipping_first_name (PRENOM)")
    shipping_first_name = driver.find_element(By.ID, "shipping_first_name")
    shipping_first_name.clear()
    shipping_first_name.send_keys(PRENOM)

    print("start fill shipping_last_name (NOM)")
    shipping_last_name = driver.find_element(By.ID, "shipping_last_name")
    shipping_last_name.clear()
    shipping_last_name.send_keys(NOM)

    print("start fill shipping_country_element (PAYS)")
    shipping_country_element = driver.find_element(By.ID, "shipping_country")
    shipping_country_selector = Select(shipping_country_element)
    shipping_country_selector.select_by_value(PAYS)

    print("start fill shipping_address_1 (ADRESSE_NUMERO_NOM_RUE)")
    shipping_address_1 = driver.find_element(By.ID, "shipping_address_1")
    shipping_address_1.clear()
    shipping_address_1.send_keys(ADRESSE_NUMERO_NOM_RUE)

    print("start fill shipping_address_2 (ADRESSE_BATIMENT_APPARTEMENT)")
    shipping_address_2 = driver.find_element(By.ID, "shipping_address_2")
    shipping_address_2.clear()
    shipping_address_2.send_keys(ADRESSE_BATIMENT_APPARTEMENT)

    print("start fill shipping_postcode (CODE_POSTAL)")
    shipping_postcode = driver.find_element(By.ID, "shipping_postcode")
    shipping_postcode.clear()
    shipping_postcode.send_keys(CODE_POSTAL)

    print("start fill shipping_city (VILLE)")
    shipping_city = driver.find_element(By.ID, "shipping_city")
    shipping_city.clear()
    shipping_city.send_keys(VILLE)

    print("start fill shipping_phone (TELEPHONE)")
    shipping_phone = driver.find_element(By.ID, "shipping_phone")
    shipping_phone.clear()
    shipping_phone.send_keys(TELEPHONE)

    print("start fill cardholder (NOM_PROPRIETAIRE_CARTE_BLEU)")
    # go inside to frame for credit card holder name
    iframe = driver.find_element(By.ID, "cardholder")
    driver.switch_to.frame(iframe)
    credit_card_holder_name = driver.find_element(By.ID, "cardholder")
    credit_card_holder_name.clear()
    credit_card_holder_name.send_keys(NOM_PROPRIETAIRE_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    print("start fill credit-cart-number (NUMERO_CARTE_BLEU)")
    # go inside to frame for credit card number
    iframe = driver.find_element(By.ID, "pan")
    driver.switch_to.frame(iframe)
    credit_card_number = driver.find_element(By.ID, "credit-card-number")
    credit_card_number.clear()
    credit_card_number.send_keys(NUMERO_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    print("start fill expiration (DATE_EXPIRATION_CARTE_BLEU)")
    # go inside to frame for credit card expiration
    iframe = driver.find_element(By.ID, "exp")
    driver.switch_to.frame(iframe)
    credit_card_exp = driver.find_element(By.ID, "expiration")
    credit_card_exp.clear()
    credit_card_exp.send_keys(DATE_EXPIRATION_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    print("start fill cvv (NUMERO_SECURITE_CARTE_BLEU)")
    # go inside to frame for credit card secure number
    iframe = driver.find_element(By.ID, "cvv")
    driver.switch_to.frame(iframe)
    credit_card_secure_number = driver.find_element(By.ID, "cvv")
    credit_card_secure_number.clear()
    credit_card_secure_number.send_keys(NUMERO_SECURITE_CARTE_BLEU)
    # get out of frame
    driver.switch_to.default_content()

    print("start fill shipping method (METHODE_ENVOI)")
    radio_button = driver.find_element(By.ID, METHODE_ENVOI)
    driver.execute_script("arguments[0].click();", radio_button)
    if METHODE_ENVOI == 'shipping_method_0_lpc_relay59':
        print("shipping methode pickup-point")

        pickup_button = None
        while pickup_button is None:
            try:
                pickup_button = driver.find_element(By.ID, "lpc_pick_up_widget_show_map")
            except NoSuchElementException:
                print("pickup_button not found, wait for loading...")
                time.sleep(0.5)
        print("found pickup-button")

        pickup_point_already_selected = False
        if "Changer le point de retrait" in pickup_button.text:
            # POINT RELAIS DEJA PRESELECTIONNE
            pickup_name_selected = driver.find_element(By.CSS_SELECTOR, "div.lpc_pickup_info_address_name")
            if NOM_ZONE_POINT_RELAIS in pickup_name_selected.text or pickup_name_selected.text in NOM_ZONE_POINT_RELAIS:
                print("Good pickup-point already selected")
                pickup_point_already_selected = True
        if not pickup_point_already_selected or action == "choose_pickup_point":
            # PAS DE POINT RELAIS PRESELECTIONNE
            # OU POINT RELAIS PRESELECTIONNE  QUI N EST PAS LE BON
            # OU USER VEUT ACCEDER A POINT RELAIS
            print("Select pickup-point")
            choose_pickup_point(driver, action)

    if action == "buy":
        print("start Command Validation ")
        button_validation = driver.find_element(By.ID, "place_order")
        #driver.execute_script("arguments[0].click();", button_validation)
        print("You succeeded in buying the product!")
    if action == "test":
        print("")
        print("--- --- ---")
        print("You can now verify all parameters. If there is a mistake, change parameters on your selected config file.")
        input("Click ENTER to continue(no product will be buy)")

    print("Command done")


def choose_pickup_point(driver, action):
    config_file = config_file_manager.get_config_file()
    ADRESSE_CODE_POSTAL_ZONE_POINT_RETRAIT = config_file['VARIABLEFORM']['ADRESSE_CODE_POSTAL_ZONE_POINT_RETRAIT']
    NOM_ZONE_POINT_RELAIS = config_file['VARIABLEFORM']['NOM_ZONE_POINT_RELAIS']

    print("click on select pickup-point button")
    element = driver.find_element(By.ID, "lpc_pick_up_widget_show_map")
    driver.execute_script("arguments[0].click();", element)
    print("write address on pickup-point pop-up")
    adress_input = driver.find_element(By.ID, "widget_colissimo_adresse")
    adress_input.clear()
    adress_input.send_keys(ADRESSE_CODE_POSTAL_ZONE_POINT_RETRAIT)
    print("select first address available on dynamic list")
    table = driver.find_element(By.ID, "widget_colissimo_autocomplete")
    time.sleep(5)
    choose_first_adress = table.find_element(By.CSS_SELECTOR, "td.widget_colissimo_autocomplete_li")
    driver.execute_script("arguments[0].click();", choose_first_adress)
    print("click on loup element")
    loup_element = driver.find_element(By.CLASS_NAME, "widget_colissimo_loupe_img")
    driver.execute_script("arguments[0].click();", loup_element)
    print("research on list pickup-point element by name")
    time.sleep(5)
    if action == "choose_pickup_point":
        print("")
        print("--- --- --- ---")
        print("You now have access to the pickup points.")
        print("Please copy and paste the name of the selected pickup point into your config file under the variable NOM_ZONE_POINT_RELAIS.")
        input("Press ENTER to continue")
        return
    pickup_elements = driver.find_elements(By.CSS_SELECTOR, "div.widget_colissimo_PDR")
    target_pickup_element = None
    for pickup_element in pickup_elements:
        try:
            pickup_name = pickup_element.find_element(By.CSS_SELECTOR, "p.widget_colissimo_text_bold")
            if NOM_ZONE_POINT_RELAIS in pickup_name.text.strip().upper():
                target_pickup_element = pickup_element
                print("find selected pickup-point: ", pickup_name.text.strip().upper())
                break
        except:
            continue
    if target_pickup_element == None:
        print("NOT FOUND SELECTED PICKUP-POINT, GET FIRST PICKUP-POINT BY DEFAULT")
        target_pickup_element = pickup_elements[0]
    print("open good pickup-point element")
    button_for_open_right_element = target_pickup_element.find_element(By.CSS_SELECTOR, "img.widget_colissimo_icone_coche")
    driver.execute_script("arguments[0].click();", button_for_open_right_element)
    print("select good pickup-point element")
    button_for_select_right_element = target_pickup_element.find_element(By.CSS_SELECTOR, "div.widget_colissimo_bouton_validation")
    driver.execute_script("arguments[0].click();", button_for_select_right_element)
    print("good pickup-point selected")
