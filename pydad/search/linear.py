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
from typing import List, Optional


def linear(seq: List[int], key: int) -> Optional[int]:
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return None


def linear_v1(seq: List[int], key: int):
    for k, v in enumerate(seq):
        if v == key:
            return k
    return None


if __name__ == "__main__":
    # print(linear([1,2,3], 5))
    print(linear_v1([1,2,3,4,5], 5))
