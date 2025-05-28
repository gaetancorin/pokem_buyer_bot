import datetime
import requests
import App.utils.config_file_manager as config_file_manager
from bs4 import BeautifulSoup
import App.utils.session_manager as session_manager
import App.generate_connection as generate_connection
import App.dev_utils.file_saver as file_saver

def live_check_disponibility():
    compteur = 0
    time_start = datetime.datetime.now()
    response = 200
    button = None
    url_to_post = None
    product_id = None
    gtm4wp_product_data = None
    price_to_one_product = None
    time_last_refresh_account =  datetime.datetime.now()
    while response != 200 or button is None or url_to_post is None or product_id is None or gtm4wp_product_data is None or price_to_one_product is None:

        # keep session alive if more than 5 minutes
        if (datetime.datetime.now() - time_last_refresh_account) > datetime.timedelta(minutes=5):
            time_last_refresh_account = datetime.datetime.now()
            print("refresh waiting account")
            session_manager.force_new_session()
            print("---- GET PROOF_ID OF CONNECTION (refresh) ----")
            proof_id = generate_connection.get_proof_of_connection()
            print("---- GET COOKIES (refresh) ----")
            generate_connection.ask_for_cookies(proof_id)
            print("---- TEST CONNECTION (refresh) ----")
            generate_connection.connect_by_cookies()

        # check product disponibility
        response, button, url_to_post, product_id, gtm4wp_product_data, price_to_one_product = check_disponibility(compteur, time_start)
        compteur += 1
        #time.sleep(0.1)

        if response == 200 and button is not None:
            if url_to_post is None or product_id is None or gtm4wp_product_data is None or price_to_one_product is None:
                print("FATAL ERROR ON HTML scrapping even if status_code 200 and button OK")
    return url_to_post, product_id, gtm4wp_product_data, price_to_one_product


def check_disponibility(compteur, time_start):
    config_file = config_file_manager.get_config_file()
    url_product_card = config_file['VARIABLEENV']['URLPRODUCTCARD'].replace("(do_not_mention)", "")

    time_now = datetime.datetime.now()
    time_start_compteur = time_now - time_start
    response = requests.get(url_product_card)
    if response.status_code != 200:
        print("FAIL ON STATUS-CODE, STATUS CODE: ", response.status_code, " // ", time_now.strftime("%Hh%Mm%Ss"),
              "compteur:", compteur, "time_start:", time_start_compteur)
        return response.status_code, None, None, None, None, None

    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form', {'action': url_product_card})
    if not form:
        print("Wait Product Disponibility (buy button not found) STATUS CODE:", response.status_code, "//", time_now.strftime("%Hh%Mm%Ss"), "counter:", compteur, "time_start:", time_start_compteur)
        # en mode debug, écrire le code html recu si bouton pas trouvé
        # file_saver.save_html_file_for_futur_analysis(file_name="check_disponibility_not_button", response=response)
        return response.status_code, form, None, None, None, None
    else:
        print("button ok, status code:", response.status_code, " // ", time_now.strftime("%Hh%Mm%Ss"), "compteur:", compteur, "time_start:", time_start_compteur)
        url_to_post = form['action']
        gtm4wp_product_data = form.find('input', {'name': 'gtm4wp_product_data'})['value']
        product_id = soup.find('link', {'rel': 'shortlink'})['href'].split('p=')[1]
        price_to_one_product = soup.find("p", class_="price").find("span", class_="woocommerce-Price-amount amount")
        price_to_one_product = price_to_one_product.find("bdi").find(text=True, recursive=False).strip().replace(',', '.')
        print("price to one product:", price_to_one_product)
        print("product_id = ", product_id)
        print("url_to_post = ", url_to_post)
        print("gtm4wp_product_data = ", gtm4wp_product_data)
        return response.status_code, form, url_to_post, product_id, gtm4wp_product_data, price_to_one_product



if __name__ == "__main__":
    config_file_manager.set_config_file_on_debug_mode(1)
    print("---- START VERIFY DISPONIBILITY ----")
    live_check_disponibility()
    print("---- END -----")
