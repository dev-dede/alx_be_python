import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(2, 8), 10)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(-2, 5), 3)
    def test_substract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(5, 10), -5)
        self.assertEqual(self.calculator.subtract(-10, -5), -5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, -3), 6)
        self.assertEqual(self.calculator.multiply(2, -3), -6)
        self.assertEqual(self.calculator.multiply(2, 0), 0)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(3, 2), 1.5)
        self.assertEqual(self.calculator.divide(0, 2), 0)
        self.assertEqual(self.calculator.divide(9.6, 2), 4.8)
        self.assertEqual(self.calculator.divide(2, 0), None)