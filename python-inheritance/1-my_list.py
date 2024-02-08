#!/usr/bin/python3
"""The MyList module"""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """fucn is docced"""
        sorted_list = sorted(self)
        print(sorted_list)
