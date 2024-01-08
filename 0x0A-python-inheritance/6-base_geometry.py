#!/usr/bin/python3
"""
contains the class BaseGeometry
"""


class BaseGeometry:
    """a class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
