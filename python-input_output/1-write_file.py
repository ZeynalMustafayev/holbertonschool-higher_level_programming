#!/usr/bin/python3
"""writing file"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, "w") as file:
        return file.write(text)
