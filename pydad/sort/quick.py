#!/usr/bin/env python3
"""
quick.py for quick sort.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 02:52:27 AM EST

DESCRIPTION:
快速排序
"""
from typing import List


def quick(seq: list) -> list:
    if len(seq) < 2:
        return seq
    pivot = seq.pop()
    greater: List[int] = []
    lesser: List[int] = []
    for element in seq:
        (greater if element > pivot else lesser).append(element)
    return quick(lesser) + [pivot] + quick(greater)

def quick_v2(seq: List[int]) -> List[int]:
    if len(seq) < 2:
        return seq
    pivot = seq.pop()
    greater = [x for x in seq if x > pivot]
    lesser = [x for x in seq if x <= pivot]
    return quick(lesser) + [pivot] + quick(greater)


if __name__ == "__main__":
    print(quick([3, 6, 8, 10, 1, 2, 1]))
    print(quick_v2([3, 6, 8, 10, 1, 2, 1]))
