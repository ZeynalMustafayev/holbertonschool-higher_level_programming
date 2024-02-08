#!/usr/bin/python3

"""
    The ``MyList`` module
"""


class MyList(list):
    """mylist class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
