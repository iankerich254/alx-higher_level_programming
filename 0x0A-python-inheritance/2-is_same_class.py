#!/usr/bin/python3
"""
module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is exact class a_class,else false"""
    return (type(obj) is a_class)
