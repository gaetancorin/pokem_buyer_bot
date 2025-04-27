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
    # while response == 200:
    while response == 200 and button == None:
        response, button = check_disponibility(compteur, time_start, write_html=False)
    compteur += 1
    # time.sleep(0.1)

def check_disponibility(compteur, time_start, write_html=False):
    time_now = datetime.datetime.now()
    time_start_compteur = time_now - time_start
    response = requests.get(url_product_card)

    soup = BeautifulSoup(response.text, "html.parser")
    form = soup.find('form', {'action': url_product_card})
    if form:
        print("button ok, status code:", response.status_code, " // ", time_now.strftime("%Hh%Mm%Ss"), "compteur:", compteur, "time_start:", time_start_compteur)
    else:
        print("BUTTON NOT FOUND, STATUS CODE: ", response.status_code, " // ", time_now.strftime("%Hh%Mm%Ss"),
              "compteur:", compteur, "time_start:", time_start_compteur)
        # écrire le code html recu si bouton pas trouvé
        if write_html == True:
            Path("../outpout/").mkdir(parents=True, exist_ok=True)
            with open("../outpout/outpout_fail.html", "w", encoding="utf-8") as f:
                f.write(response.text)
    return response.status_code, form

if __name__ == "__main__":
    print("---- START VERIFY DISPONIBILITY ----")
    live_check_disponibility()
    print("---- END -----")
