import requests

session = None

def get_session():
    global session
    if session is None:
        session = requests.Session()
    return session

def force_new_session():
    global session
    session = requests.Session()
    return session