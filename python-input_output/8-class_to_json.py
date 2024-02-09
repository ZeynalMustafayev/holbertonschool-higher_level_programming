#!/usr/bin/python3
"""json"""


def class_to_json(obj):
    """Initialize an empty dictionary"""
    json_dict = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
