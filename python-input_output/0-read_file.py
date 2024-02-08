#!/usr/bin/python3
"""Reading file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
