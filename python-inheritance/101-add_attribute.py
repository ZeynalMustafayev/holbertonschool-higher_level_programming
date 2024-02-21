#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attr_name, attr_value):
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
