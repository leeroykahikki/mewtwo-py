import unittest
from unittest.suite import TestSuite
from mewtwo.example.example import plus_example, minus_example, division_example, multiplication_example

class MyTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus_example(5, 5), 10)

    def test_minus(self):
        self.assertEqual(minus_example(1, 1), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication_example(3, 3), 9)

    def test_division(self):
        self.assertEqual(division_example(6, 2), 3)


if __name__ == "__main__":
    suite = TestSuite()
    tests = unittest.TestLoader()

    suite.addTest(tests.loadTestsFromTestCase(MyTestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)
