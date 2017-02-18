import random, hashlib, json

with open('secret.json') as json_data:
    SECRET = json.load(json_data)['secret']

def make_cookie_hash(cookie):
    return str(hashlib.sha256(str(cookie) + SECRET).hexdigest())


def make_cookie(cookie):
    return str(cookie) + "|" + make_cookie_hash(cookie)


def check_cookie(cookie):
    if cookie:
        (cookieVal, hashStr) = cookie.split('|')
    else:
        return None
    return cookieVal if make_cookie_hash(cookieVal) == hashStr else None