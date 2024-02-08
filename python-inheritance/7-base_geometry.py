#!/usr/bin/python3
"""
    The ``MyList`` module
"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """fucn is docced"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """fucn is docced"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
