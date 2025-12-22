import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Subtraction tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    # --- Multiplication tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # --- Division tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_result_is_float(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()
