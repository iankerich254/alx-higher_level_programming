#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for elmt in my_list:
            new_list.append(False if elmt % 2 else True)
    return new_list
