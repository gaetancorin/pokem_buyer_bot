# this util help to debug by displaying cookies for each steps on terminal
cookies_displayed = False

def displayed_cookies_if_activated(session):
    if cookies_displayed != True:
        return
    else:
        print("Cookies reçus :")
        for cookie in session.cookies:
            print("session | ", cookie.name, "=", cookie.value)
            # print("session | ", cookie.name, "=", cookie.value, "domain": cookie.domain, "path": cookie.path}")
