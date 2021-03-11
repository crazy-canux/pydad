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
"""


def insertion_sort(seq: list) -> list:
    for insert_index, insert_value in enumerate(seq[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < seq[insert_index]:
            seq[insert_index+1] = seq[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            seq[insert_index+1] = insert_value
    return seq
