import os
import unittest
import sys
sys.path.insert(0, os.path.abspath(".."))

from pydad.datastructure.fibonacci import *


class FibonacciTest(unittest.TestCase):
    def test_get_fib_value(self):
        self.assertEqual(
            0, get_fib_value(0), msg="Get fib 0 failed."
        )
        self.assertEqual(
            1, get_fib_value(1), msg="Get fib 1 failed."
        )
        self.assertEqual(
            1, get_fib_value(2), msg="Get fib 2 failed."
        )
        self.assertEqual(
            2, get_fib_value(3), msg="Get fib 3 failed."
        )

    def test_get_fib_value_by_for(self):
        self.assertEqual(
            0, get_fib_value_by_for(0), msg="Get fib 0 failed."
        )
        self.assertEqual(
            1, get_fib_value_by_for(1), msg="Get fib 1 failed."
        )
        self.assertEqual(
            1, get_fib_value_by_for(2), msg="Get fib 2 failed."
        )
        self.assertEqual(
            2, get_fib_value_by_for(3), msg="Get fib 3 failed."
        )


if __name__ == "__main__":
    unittest.main()
