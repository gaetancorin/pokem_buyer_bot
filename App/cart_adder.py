from App.utils import session_manager as session_manager
import App.dev_utils.cookies_manager as cookies_manager

def add_product_in_cart(url_to_post, product_id, gtm4wp_product_data):
    url = url_to_post
    data = {
        "quantity": 1,
        "add-to-cart": product_id,
        "gtm4wp_product_data": gtm4wp_product_data
    }
    session = session_manager.get_session()

    for i in range(1): ############## more than 1 if simulate buy multiple same product
        response = session.post(url, data=data)
        print("Statut:", response.status_code)
        if response.status_code == 504:
            return None
        # print("Contenu:", response.text)
        cookies_manager.displayed_cookies_if_activated(session)
    return response.status_code, response.text
