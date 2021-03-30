#!/usr/bin/env python3
"""
interpolation.py for interpolation search.

Copyright (C) 2021 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2021 01:10:07 AM EST

DESCRIPTION:
"""
from typing import List


def interpolation(seq: List[int], key: int):
    min = 0
    max = len(seq) - 1

    while min <= max:
        # make sure denominator != 0
        if seq[min] == seq[max]:
            if seq[min] == key:
                return min
            else:
                return None

        point = min + ((key - seq[min]) * (max - min)) // (seq[max] - seq[min])

        # make sure index not out of range.
        if point < 0 or point >= len(seq):
            return None

        if key == seq[point]:
            return point
        else:
            if point < min:
                max = min
                min = point
            elif point > max:
                max = point
                min = max
            else:
                if key < seq[point]:
                    max = point - 1
                else:
                    min = point + 1
        return None





