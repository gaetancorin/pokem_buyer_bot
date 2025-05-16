import time
import datetime
import requests
import configparser
from bs4 import BeautifulSoup
from pathlib import Path

config = configparser.ConfigParser()
config.read('../config/config.ini')
url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

def live_check_disponibility():
    compteur = 0
    time_start = datetime.datetime.now()
    response = 200
    button = None
    url_to_post = None
    product_id = None
    gtm4wp_product_data = None
    price_to_one_product = None
    while response != 200 or button is None or url_to_post is None or product_id is None or gtm4wp_product_data is None or price_to_one_product is None:
        response, button, url_to_post, product_id, gtm4wp_product_data, price_to_one_product = check_disponibility(compteur, time_start, write_html=False)
        compteur += 1
        # time.sleep(0.1)

        if response == 200 and button is not None:
            if url_to_post is None or product_id is None or gtm4wp_product_data is None or price_to_one_product is None:
                print("FATAL ERROR ON HTML scrapping even if status_code 200 and button OK")
    return url_to_post, product_id, gtm4wp_product_data, price_to_one_product


def check_disponibility(compteur, time_start, write_html=False):
    time_now = datetime.datetime.now()
    time_start_compteur = time_now - time_start
    response = requests.get(url_product_card)

    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form', {'action': url_product_card})
    if not form:
        print("BUTTON NOT FOUND, STATUS CODE: ", response.status_code, " // ", time_now.strftime("%Hh%Mm%Ss"),
              "compteur:", compteur, "time_start:", time_start_compteur)
        # écrire le code html recu si bouton pas trouvé
        if write_html == True:
            Path("../outpout/").mkdir(parents=True, exist_ok=True)
            with open("../outpout/outpout_fail.html", "w", encoding="utf-8") as f:
                f.write(response.text)
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
    print("---- START VERIFY DISPONIBILITY ----")
    live_check_disponibility()
    print("---- END -----")
