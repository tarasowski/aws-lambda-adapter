import unittest
from business import add, subtract, multiply, divide


class TestHandler(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)

if __name__ == "__main__":
    unittest.main()