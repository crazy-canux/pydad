#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bubble_sort.py for sort algorithm for bubble sort.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 02:52:27 AM EST

DESCRIPTION:
"""


def bubble_sort(seq):
    """Main function for bubble sort from min to max.

    :param seq: include string/tupple/list.
    :type seq: sequence.
    :return seq: return the result after bubble sort.
    :rtype: sequence.
    """
    length = len(seq)
    for i in range(length):
        for j in range(1, length-i):
            if seq[j] < seq[j-1]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
    return seq


def bubble_sort_desc(seq):
    """Main function for bubble sort from max to min.

    :param seq: include string/tupple/list.
    :type seq: sequence.
    :return seq: return the result after bubble sort with descending.
    :rtype seq: sequence.
    """
    length = len(seq)
    for i in range(length):
        for j in range(1, length-i):
            if seq[j] > seq[j-1]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
    return seq


if __name__ == "__main__":
    seq = [200, 59, -6, 67, 0, 18, 59]
    print("source seq: {}".format(seq))
    print("after bubble sort: {}".format(bubble_sort(seq)))
    print("after bubble sort desc: {}".format(bubble_sort_desc(seq)))
