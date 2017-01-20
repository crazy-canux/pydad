#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sequential_search.py for search algorithm sequential.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2017 01:08:39 AM EST

DESCRIPTION:
"""


def sequential_search(seq, key):
    """Main function for sequential search algorithm.

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
    return False


if __name__ == "__main__":
    seq = [157, 27, -8, 4895, 0, -49]
    key = -8
    print("index: {0}, in seq: {1}, is the same with key: {2}.".format(sequential_search(seq, key), seq, key))
