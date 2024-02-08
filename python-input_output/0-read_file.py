#!/usr/bin/python3
"""Reading file"""


def read_file(filename=""):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except:
        pass
