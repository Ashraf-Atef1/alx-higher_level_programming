#!/usr/bin/python3
"""
This module contain BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif not value > 0:
            raise ValueError(f"{name} must be greater than 0")
