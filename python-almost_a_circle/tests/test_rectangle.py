import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3, 4)
        self.r3 = Rectangle(1, 1, 1, 1, 1)

        self.new_dictionary = {"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}
        self.r1_list = [self.r1]
    
    #Test cases
    def test_rectangle(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.y, 1)
        self.assertEqual(self.r3.id, 1)

        """TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")


        """ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
    
    #Test area
    def test_area(self):
        self.assertEqual(self.r1.area(), 2)
