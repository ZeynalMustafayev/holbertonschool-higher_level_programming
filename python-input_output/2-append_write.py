#!/usr/bin/python3
"""Reading file"""


def append_write(filename="", text=""):
    """append the file"""
    with open(filename, "a") as file:
        return file.write(text)
