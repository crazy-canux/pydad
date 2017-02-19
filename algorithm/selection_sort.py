#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
selection_sort.py for sort algorithm selection.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 01:02:49 AM EST

DESCRIPTION:
"""


def selection_sort(seq):
    """Main function for sort algorithm sort from min to max.

    :param seq: a sequence can be string, tupple, list.
    :type seq: sequence.
    :return seq: return a sequence after sort.
    :rtype seq: sequence.
    """
    for i in range(0, len(seq)):
        print("====={}=====".format(i))
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[min_index] > seq[j]:
                min_index = j
                print(min_index)
        if min_index != i:
            print(seq)
            seq[i], seq[min_index] = seq[min_index], seq[i]
            print(seq)
    return seq


def selection_sort_desc(seq):
    """Main function for sort algorithm sort from max to min.

    :param seq: a sequence can be string, tupple, list.
    :type seq: sequence.
    :return seq: return a sequence after sort.
    :rtype: sequence.
    """
    for i in range(0, len(seq)):
        max_index = i
        for j in range(i+1, len(seq)):
            if seq[max_index] < seq[j]:
                max_index = j
        if max_index != i:
            seq[i], seq[max_index] = seq[max_index], seq[i]
    return seq


if __name__ == "__main__":
    seq = [200, 59, -6, 67, 0, 18, 59]
    print("source seq: {}".format(seq))
    print("after selection_sort: {}".format(selection_sort(seq)))
    print("after selection_sort_desc: {}".format(selection_sort_desc(seq)))
