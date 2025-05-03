
cookies_storage = {}

def add_cookies(key, value, domain, path):
    global cookies_storage
    cookies_storage[key] = {"value": value, "domain": domain, "path": path}

def get_cookies():
    global cookies_storage
    return cookies_storage
