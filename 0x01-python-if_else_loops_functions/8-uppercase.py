#!/usr/bin/python3
def to_uper_ke(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(string):
    string_new = ""
    for character in string:
        string_new += "%c" % to_uper_ke(character)
    print("{:s}".format(string_new))
