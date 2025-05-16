import App.generate_connection as generate_connection
import App.cart_cleaner as cart_cleaner
import App.verify_disponibility as verify_disponibility
import App.cart_adder as cart_adder
import App.cart_final_check as cart_final_check
import App.buy_cart as buy_cart
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

    product_in_cart = None
    while product_in_cart == None:
        print("---- CLEAN CART ----")
        cart_cleaner.clean_cart_if_product()
        print("---- LOOP CHECKING PRODUCT AVAILABILITY (without connect)----")
        url_to_post, product_id, gtm4wp_product_data, price_one_product = verify_disponibility.live_check_disponibility()

        print("---- ADD PRODUCT IN CART (connect)----")
        status_code_when_add, html_when_add = cart_adder.add_product_in_cart(url_to_post, product_id, gtm4wp_product_data)
        print("---- FINAL CHECK ORDER VALIDATION (connect)----")
        product_in_cart = cart_final_check.final_check_order_validation(status_code_when_add, html_when_add, price_one_product)

    print("---- BUY CART (connect)----")
    buy_cart.place_order_by_selenium()
    print("---- END -----")
