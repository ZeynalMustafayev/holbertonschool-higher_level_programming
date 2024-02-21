#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attr_name, attr_value):
    """add attribute"""
    setattr(obj, attr_name, attr_value)
    if not hasattr(obj, attr_name) or getattr(obj, attr_name) != attr_value:
        raise TypeError("can't add new attribute")
