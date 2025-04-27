import App.generate_connection as generate_connection
import App.verify_disponibility as verify_disponibility
import requests
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
username = config['VARIABLEENV']['USERNAME']
password = config['VARIABLEENV']['PASSWORD']

session = requests.Session()

if __name__ == "__main__":
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = generate_connection.get_proof_of_connection()
    print("---- GET COOKIES ----")
    generate_connection.ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    generate_connection.connect_by_cookies()
    print("---- END -----")
