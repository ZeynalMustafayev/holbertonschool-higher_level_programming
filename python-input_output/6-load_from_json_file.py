#!/usr/bin/python3
"""json"""


import json


def load_from_json_file(filename):
    """to json string"""
    with open(filename, "r") as file:
        return json.load(file)
