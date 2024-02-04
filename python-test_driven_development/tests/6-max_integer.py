#!/usr/bin/python3

import unittest


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    #Positive integers
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    #None case
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    #Negative numbers
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
    
    #Both negative and positive numbers
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    #Only one element
    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)


if __name__ == "__main__":
    unittest.main()
