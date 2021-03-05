import unittest

from pydad.sort.selection import selection_sort
from pydad.sort.bubble import bubble_sort
from pydad.sort.quick import quick_sort


class SortTestCase(unittest.TestCase):
    def test_bubble(self):
        seq = [23, 78, -25, 82, 0, 396]
        res = bubble_sort(seq)
        print(res)
        self.assertEqual(
            res[0], -25,
            msg='bubble sort failed.'
        )
        self.assertEqual(
            res[-1], 396,
            msg='bubble sort failed.'
        )

    def test_selection(self):
        seq = [23, 78, -25, 82, 0, 396]
        res1 = selection_sort(seq)
        print(res1)
        self.assertEqual(
            res1[0], -25,
            msg='selection sort failed.'
        )
        self.assertEqual(
            res1[-1], 396,
            msg='selection sort failed.'
        )

    def test_quick(self):
        seq = [23, 78, -25, 82, 0, 396]
        res2 = quick_sort(seq)
        print(res2)
        self.assertEqual(
            res2[0], -25,
            msg='quick sort failed'
        )
        self.assertEqual(
            res2[-1], 396,
            msg='quick sort failed.'
        )


if __name__ == '__main__':
    unittest.main()
