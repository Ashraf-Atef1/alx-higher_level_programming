#!/bin/usr/python3
""" 0-add_integer.py: add integer module """


def add_integer(a, b=98):
    """add up to two integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    
    doctest.testfile("tests/0-add_integer.txt")
