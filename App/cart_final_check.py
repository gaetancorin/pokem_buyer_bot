from App.utils import session_manager as session_manager
import App.utils.cookies_manager as cookies_manager
from bs4 import BeautifulSoup

def final_check_order_validation(status_code_when_add, html_when_add, price_one_product):
    if status_code_when_add == 200:
        print("status_code_when_add is 200, look response for check order")

        soup = BeautifulSoup(html_when_add, "html.parser")
        number_products_in_cart = soup.find("span", class_="elementor-button-icon-qty").get("data-counter")
        print("number products in cart:", number_products_in_cart)

        price_in_cart = soup.find("span", class_="elementor-button-text")
        price_in_cart = price_in_cart.find("span", class_="woocommerce-Price-amount amount")
        price_in_cart = price_in_cart.find("bdi").find(text=True, recursive=False).strip().replace(',', '.')
        print("price in cart:", price_in_cart)

        price_one_product = soup.find("p", class_="price")
        price_one_product = price_one_product.find("span", class_="woocommerce-Price-amount amount")
        price_one_product = price_one_product.find("bdi").find(text=True, recursive=False).strip().replace(',', '.')
        print("price to one product:", price_one_product)

    else:
        print("status_code_when_add is NOT 200, need to get cart for check order")

        url = "https://www.cardshunter.fr/commander/"
        session = session_manager.get_session()
        response = None
        while not response or response.status_code != 200:
            response = session.get(url)
            print("Statut:", response.status_code)
        # print(response.text)
        cookies_manager.displayed_cookies_if_activated(session)

        soup = BeautifulSoup(response.text, "html.parser")
        number_products_in_cart = soup.find("td", class_="product-name")
        if number_products_in_cart == None:
            print("CART IS EMPTY")
            return None
        number_products_in_cart = number_products_in_cart.find("strong", class_="product-quantity").get_text()
        number_products_in_cart = number_products_in_cart.split()[-1]
        print("number products in cart:", number_products_in_cart)

        price_in_cart = soup.find("tr", class_="cart-subtotal").find("bdi").find(text=True, recursive=False).strip().replace(',', '.')
        print("price in cart:", price_in_cart)
        print("price to one product:", price_one_product)

    # Laisse une marge de 20% du prix du produit au cas ou
    if number_products_in_cart == '1' and float(price_in_cart) < (float(price_one_product) * 1.2):
        print("final check order validation DONE")
        return "Done"
    else:
        print("CONDITIONS FOR CART FINAL CHECK IS FAILED, retry to add product")
        return None
