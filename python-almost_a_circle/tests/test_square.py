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
        self.new_dictionary = {"id": 1, "size": 1, "x": 1, "y": 1}
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

        """ValueError"""
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(0, 2)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    #Test str
    def test_str(self):
        self.assertEqual(self.s4.__str__(), "[Square] (4) 2/3 - 1")

    #Test update
    def test_update(self):
        self.s3.update(1, 1, 1, 1, 1)
        self.assertEqual(str(self.s3), "[Square] (1) 1/1 - 1")

    #Test create
    def test_create(self):
        new = Square.create(**self.new_dictionary)
        self.assertEqual(str(new), "[Square] (1) 1/1 - 1")

    def tearDown(self):
        try:
            os.remove("Square.json")
        except:
            pass
