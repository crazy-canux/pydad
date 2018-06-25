import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(".."))

from pydad.datastructure.fibonacci import *


class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(
            0, fibonacci(0), msg="Get fib 0 failed."
        )
        self.assertEqual(
            1, fibonacci(1), msg="Get fib 1 failed."
        )
        self.assertEqual(
            1, fibonacci(2), msg="Get fib 2 failed."
        )
        self.assertEqual(
            2, fibonacci(3), msg="Get fib 3 failed."
        )

    def test_fibonacci_by_array(self):
        self.assertEqual(
            0, fibonacci_array(0), msg="Get fib 0 failed."
        )
        self.assertEqual(
            1, fibonacci_array(1), msg="Get fib 1 failed."
        )
        self.assertEqual(
            1, fibonacci_array(2), msg="Get fib 2 failed."
        )
        self.assertEqual(
            2, fibonacci_array(3), msg="Get fib 3 failed."
        )


if __name__ == "__main__":
    unittest.main()
