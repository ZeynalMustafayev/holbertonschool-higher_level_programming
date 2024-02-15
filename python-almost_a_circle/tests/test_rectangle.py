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

    #Test str
    def test_str(self):
        self.assertEqual(self.r3.__str__(), "[Rectangle] (1) 1/1 - 1/1")

    #Test display
    def test_display(self):
        output = "#\n#\n"
        with patch("sys.stdout", new=StringIO()) as o:
            self.r1.display()
            self.assertEqual(o.getvalue(), output)
        output = "\n #\n"
        with patch("sys.stdout", new=StringIO()) as out:
            self.r3.display()
            self.assertEqual(out.getvalue(), output)

    #Test dictionary 
    def test_dictionary(self):
        self.assertEqual(self.r3.to_dictionary(), {"width": 1, "height": 1, "x": 1, "y": 1, "id": 1})

    #Test update
    def test_update(self):
        self.r3.update(1, 1, 1, 1, 1)
        self.assertEqual(str(self.r3), "[Rectangle] (1) 1/1 - 1/1")

    #Test create
    def test_create(self):
        new = Rectangle.create(**self.new_dictionary)
        self.assertEqual(str(new), "[Rectangle] (1) 1/1 - 1/1")

    #Test save_to_file
    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    #Test
    def test_save_to_file_case_2(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_data(self):
        Rectangle.save_to_file([Rectangle(1, 2, id=1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]')

    #Test load_from_file
    #def test_load(self):
        #self.assertEqual(Rectangle.load_from_file(), [])

        #Rectangle.save_to_file(self.r1_list)
        #self.assertEqual(self.r1_list[0].__str__(), Rectangle.load_from_file()[0].__str__())
