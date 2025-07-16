#!/usr/bin/env python3
"""
selection.py for selection sort.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 01:02:49 AM EST

DESCRIPTION:
time: O(n^2)
space: O(1)
"""


def selection_sort(seq):
    for i in range(len(seq)-1):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq
