#!/usr/bin/env python3
"""
binary.py for binary search.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2017 01:10:07 AM EST

DESCRIPTION:
time: O(log n)
"""
from typing import List


def binary(seq: List[int], key: int) -> int:
    min_index = 0
    max_index = len(seq) - 1
    while min_index <= max_index:
        mid = (min_index + max_index) // 2
        if seq[mid] == key:
            return mid
        elif seq[mid] < key:
            min_index = mid + 1
        else:
            max_index = mid - 1
    return -1


def binary_v1(seq: List[int], key: int) -> int:
    left, right = 0, len(seq)-1
    while left <= right:
        mid = left + right >> 1
        if seq[mid] == key:
            return mid
        elif key > seq[mid]:
            left = mid+1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    print(binary([1,2,3,4], 6))
    print(binary_v1([1,2,3,4], 3))