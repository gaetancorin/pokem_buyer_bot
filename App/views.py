import App.generate_connection as generate_connection
import App.verify_disponibility as verify_disponibility
import App.prepare_cart as prepare_cart
import App.buy_cart as buy_cart
import App.check_cookies as check_cookies
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
    url_to_post, product_id, gtm4wp_product_data, price_one_product = verify_disponibility.live_check_disponibility()

    print("---- ADD TO CART (connect)----")
    result = prepare_cart.product_in_cart(url_to_post, product_id, gtm4wp_product_data)
    if result == None:
        print("--- verify product in cart -----")
        order_validation = prepare_cart.check_order_validation(price_one_product)
    print("---- CHECK ORDER VALIDATION (connect)----")
    prepare_cart.check_order_validation(price_one_product)

    print("---- BUY CART (connect)----")
    #buy_cart.place_order(price_one_product)
    check_cookies.check_cookies()
    print("---- END -----")
