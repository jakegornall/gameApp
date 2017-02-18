import random, hashlib

def make_salt():
    '''creates randomly generated number
    for use in password hashing'''
    return random.randint(10000, 99999)


def hash_pass(keyword, salt):
    return str(hashlib.sha256(str(keyword) + str(salt)).hexdigest())