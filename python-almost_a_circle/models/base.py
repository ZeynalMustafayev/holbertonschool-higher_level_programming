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
        with open(filename, "w") as file:
            if list_objs is None:
                return file.write("[]")
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        filename = f"{cls.__name__}.json"
        with open(filename, "r") as file:
            data = file.read()
            if not data:
                return []
            dicts = cls.from_json_string(data)
            return [cls.create(**d) for d in dicts]
