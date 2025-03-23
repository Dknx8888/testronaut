import unittest
from example import add, factorial, fibonacci_recursive

class TestExample(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(5, -3), 2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_fibonacci_small_number(self):
        self.assertEqual(fibonacci_recursive(4), 3)


if __name__ == '__main__':
    unittest.main()
