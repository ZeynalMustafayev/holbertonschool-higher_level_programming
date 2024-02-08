#!/usr/bin/python3
"""
    The ``MyList`` module
"""


def inherits_from(obj, a_class):
    """fucn is docced"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
