import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-3, -2), -1)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)
    
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(6, -2), -3)

    def test_divide_byone(self):
        self.assertEqual(self.calc.divide(6, 1), 6)

    def test_divide_ZERO(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)

    def test_modulo_withself(self):
        self.assertEqual(self.calc.modulo(4, 4), 0)



if __name__ == '__main__':
    unittest.main()