#!/usr/bin/env python3
"""
bubble.py for sort search for bubble sort.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 02:52:27 AM EST

DESCRIPTION:
"""
from typing import List


def quick_sort(seq: list) -> list:
    if len(seq) < 2:
        return seq
    pivot = seq.pop()
    greater: List[int] = []
    lesser: List[int] = []
    for element in seq:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
