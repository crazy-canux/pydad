import unittest

from pydad.search.sequential import sequential
from pydad.search.binary import binary


seq1 = [23, 78, -25, 82, 0, 396]


class SearchTestCase(unittest.TestCase):
    def test_sequnetial(self):
        self.assertEqual(
            sequential(seq1, 0), 4,
            msg="find 0 failed."
        )

    def test_binary(self):
        self.assertEqual(
            binary(seq1, 0), 4,
            msg="find 0 failed."
        )


if __name__ == "__main__":
    unittest.main()
