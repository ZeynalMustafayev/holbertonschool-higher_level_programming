import unittest
from  models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(None)
        self.b3 = Base(3)
        self.b4 = Base(-5)
        self.b5 = Base("If you don't like Isa, I don't like you.")

        #test cases
    def test_instances(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, -5)
        self.assertEqual(self.b5.id, "If you don't like Isa, I don't like you.")

    #def Test_to_json_string(self):
