#!/usr/bin/env python3
"""
bubble.py for bubble sort.

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
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq
