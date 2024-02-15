import unittest
from models.square import Square
from unittest.mock import patch
from io import StringIO
import os



class TestSquare(unittest.TestCase):
    def setUp(self):
        """Instances for Square"""
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 4)
        self.new_dicts = {"id": 2, "size": 2, "x": 2, "y": 2}
        self.list_s1 = [self.s1]


