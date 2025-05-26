import App.utils.session_manager as session_manager
import App.generate_connection as generate_connection
import App.cart_cleaner as cart_cleaner
import App.verify_disponibility as verify_disponibility
import App.cart_adder as cart_adder
import App.cart_verifier as cart_verifier
import App.cart_checkout as cart_checkout
import App.utils.config_file_manager as config_file_manager


def launch_bot(action=None):
    session_manager.force_new_session()
    print("---- GET PROOF_ID OF CONNECTION ----")
    proof_id = generate_connection.get_proof_of_connection()
    print("---- GET COOKIES ----")
    generate_connection.ask_for_cookies(proof_id)
    print("---- TEST CONNECTION ----")
    result = generate_connection.connect_by_cookies()
    if result == None:
        return

    product_in_cart = None
    while product_in_cart == None:
        print("---- CLEAN CART ----")
        cart_cleaner.clean_cart_if_product()
        print("---- LOOP CHECKING PRODUCT AVAILABILITY (without connect)----")
        url_to_post, product_id, gtm4wp_product_data, price_one_product = verify_disponibility.live_check_disponibility()

        print("---- ADD PRODUCT IN CART (connect)----")
        status_code_when_add, html_when_add = cart_adder.add_product_in_cart(url_to_post, product_id, gtm4wp_product_data)
        print("---- FINAL CHECK ORDER VALIDATION (connect)----")
        product_in_cart = cart_verifier.verify_order_before_checkout(status_code_when_add, html_when_add, price_one_product)

    print("---- BUY CART (connect)----")
    cart_checkout.place_order_by_selenium(action)
    print("---- END -----")
    print("")


if __name__ == "__main__":
    config_file_manager.set_config_file_on_debug_mode(1)
    launch_bot(action="test")
