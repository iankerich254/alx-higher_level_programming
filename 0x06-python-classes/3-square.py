#!/usr/bin/python3
"""Class square"""

Class Square:
    """Represents square attributes __size (int): size of square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size

    def area(self):
        return (self.__size) ** 2
