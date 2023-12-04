#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elmt in my_list:
            if elmt > max:
                max = elmt
        return max
    return None
