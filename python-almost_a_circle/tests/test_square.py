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
        self.new_dicts = {"id": 1, "size": 1, "x": 1, "y": 1}
        self.list_s1 = [self.s1]

    def test_checker(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.id, 4)

    
        """TypeError"""
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")


    def tearDown(self):
        try:
            os.remove("Square.json")
        except:
            pass
