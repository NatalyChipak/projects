#!/usr/bin/python3.8

import sys
from string import punctuation


def check_password(pwd):
    errors = []

    if not((any(i.isupper() for i in pwd)) and (any(i.islower() for i in pwd))):
        errors.append("- Password must contain both lowercase and uppercase characters")

    if not any(i.isdigit() for i in pwd):
        errors.append("- Password must contain digits")

    if not any(i in pwd for i in punctuation):
        errors.append("- Password must contains at least one punctuation character ({})".format(punctuation))

    if len(pwd) < 14:
        errors.append("- Password must be at least 14 characters long")

    if errors:
        print("Weak password:")
        [print(i) for i in errors]
    else:
        print("Strong password")


if __name__ == '__main__':
    password = sys.argv[1]
    check_password(password)

