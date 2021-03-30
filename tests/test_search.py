import unittest

from pydad.search.linear import linear
from pydad.search.binary import binary
from pydad.search.interpolation import interpolation



class SearchTestCase(unittest.TestCase):
    def test_linear(self):
        seq = [23, 78, -25, 82, 0, 396]
        self.assertEqual(
            linear(seq, 0), 4,
            msg="find 0 failed."
        )

    def test_binary(self):
        seq = [-25, 0, 23, 82, 396]
        self.assertEqual(
            binary(seq, 0), 1,
            msg="find 0 failed."
        )

    def test_interpolation(self):
        seq = [-25, 0, 23, 82, 396]
        self.assertEqual(
            interpolation(seq, 0), 1,
            msg='find 0 failed.'
        )


if __name__ == "__main__":
    unittest.main()
