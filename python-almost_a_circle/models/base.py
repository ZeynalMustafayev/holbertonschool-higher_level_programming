#!/usr/bin/python3
"""Base class"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""
        if list_dictionaries is None:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file function"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            return "[]"
        else:
            my_list = [obj.to_dictionary() for obj in list_objs]
            with open(filename, "w") as file:
                file.write(cls.to_json_string(my_list))
