#!/usr/bin/env python3
"""
linear.py for linear search.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2017 01:08:39 AM EST

DESCRIPTION:
"""
from typing import List


def linear(seq: List[int], key: int):
    """Main function for linear search.

    :param seq: a sequence.
    :type seq: sequence.
    :param key: an element in the sequence which want to be searched.
    :type key: char or int/float/complex.
    :return index: the index of the key in the seq.
    :rtype index: int.
    """
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return None
