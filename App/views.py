import App.generate_connection as generate_connection
import App.verify_disponibility as verify_disponibility
import App.buy_product as buy_product
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')
username = config['VARIABLEENV']['USERNAME']
password = config['VARIABLEENV']['PASSWORD']

url_product_card = config['VARIABLEENV']['URLPRODUCTCARD']

if __name__ == "__main__":
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = generate_connection.get_proof_of_connection()
    print("---- GET COOKIES ----")
    generate_connection.ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    generate_connection.connect_by_cookies()

    print("---- LOOP CHECKING PRODUCT AVAILABILITY (without connect)----")
    verify_disponibility.live_check_disponibility()

    print("---- PREPARE TO CART (connect)----")
    result_1 = None
    while not result_1:
        result_1 = buy_product.prepare_to_cart(write_html=True)
    url_to_post, product_id, gtm4wp_product_data = result_1
    print("---- ADD TO CART (connect)----")
    result_2 = buy_product.product_in_cart(url_to_post, product_id, gtm4wp_product_data)
    if result_2 == None:
        print("verify product")
        buy_product.verify_product_in_cart()

    print("---- CHECK ORDER VALIDATION (connect)----")
    # buy_product.check_order_validation()
    print("---- END -----")
