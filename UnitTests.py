import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 2), 14)
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(10, 3), 3.3333333333333335)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by zero")
        
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, -2), 0.01)

    def test_gcd(self):
        self.assertEqual(self.calc.gcd(24, 16), 8)
        self.assertEqual(self.calc.gcd(17, 5), 1)
        self.assertEqual(self.calc.gcd(36, 48), 12)
        self.assertEqual(self.calc.gcd(0, 5), 5)

if __name__ == '__main__':
    unittest.main()