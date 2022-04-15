#!/usr/bin/python3.8

from random import sample
from string import (ascii_lowercase, ascii_uppercase, digits, punctuation)


def is_pwd_valid(pwd):
    if not((any(i.isupper() for i in pwd)) and (any(i.islower() for i in pwd))):
        return False
    if not any(i.isdigit() for i in pwd):
        return False
    if not any(i in pwd for i in punctuation):
        return False
    return True


def generate_pwd():
    length = 14
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase
    numbers = digits
    symbols = punctuation

    strong_pwd = lowercase + uppercase + numbers + symbols
    strong_pwd = sample(strong_pwd, length)
    strong_pwd = "".join(strong_pwd)
    return strong_pwd


def check_pwd():
    password = ""
    while not is_pwd_valid(password):
        password = generate_pwd()
    print(password)


if __name__ == '__main__':
    check_pwd()

