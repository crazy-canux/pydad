import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from pydad.sort.bubble import bubble_sort
from pydad.sort.selection import selection_sort

seq = [23, 78, -25, 82, 0, 396]


class SortTestCase(unittest.TestCase):
    def test_bubble(self):
        res = bubble_sort(seq)
        self.assertEqual(
            res[0], -25,
            msg='bubble sort failed.'
        )
        self.assertEqual(
            res[-1], 396,
            msg='bubble sort failed.'
        )

    def test_selection(self):
        res1 = selection_sort(seq)
        self.assertEqual(
            res1[0], -25,
            msg='bubble sort failed.'
        )
        self.assertEqual(
            res1[-1], 396,
            msg='bubble sort failed.'
        )


if __name__ == '__main__':
    unittest.main()
