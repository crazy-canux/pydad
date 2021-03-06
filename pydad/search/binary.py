#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
binary.py for search search binary.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2017 01:10:07 AM EST

DESCRIPTION:
"""


def binary(seq, key):
    """Main function use binary search search to find the key word in a sequence.

    :param seq: sequence can be string, tupple, list.
    :type seq: sequence.
    :param key: an element of a sequence.
    :type key: char or int/float/complex.
    :return mid_index: the index in seq for key.
    :rtype mid_index: int.
    """
    min_index = 0
    max_index = len(seq) - 1

    while min_index <= max_index:
        # mid_index = min_index + (max_index - min_index) // 2
        mid_index = (min_index + max_index) >> 1
        if key > seq[mid_index]:
            min_index = mid_index + 1
        elif key < seq[mid_index]:
            max_index = mid_index - 1
        else:
            return mid_index
    return False
