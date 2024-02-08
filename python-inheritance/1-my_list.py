#!/usr/bin/python3
"""a function  returns the list of available attributes and methods"""


class MyList(list):
    """mylist function"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
