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
from typing import List


def bubble(seq: List[int]) -> List[int]:
    length = len(seq)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


def bubble_v1(seq: List[int]) -> List[int]:
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


if __name__ == "__main__":
    print(bubble([3,6,1,9, 2]))
    print(bubble_v1([2,6,3,1,9,4]))