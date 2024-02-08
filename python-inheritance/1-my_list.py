#!/usr/bin/python3
"""a function  returns the list of available attributes and methods"""


class MyList(list):
    """mylist class"""
    def print_sorted(self):
        """print_sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
