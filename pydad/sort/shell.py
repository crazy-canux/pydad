#!/usr/bin/env python3
"""
shell.py for shell sort.

Copyright (C) 2021 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2021 01:02:49 AM EST

DESCRIPTION:
"""


def __shell(seq, gap):
    for i in range(gap, len(seq)):
        insert_value = seq[i]
        index = i
        while index >= gap and seq[index-gap] > insert_value:
            seq[index] = seq[index-gap]
            index -= gap
        if index != i:
            seq[index] = insert_value


def shell_sort(seq):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        __shell(seq, gap)
    return seq
