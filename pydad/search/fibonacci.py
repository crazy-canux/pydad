#!/usr/bin/env python3
"""
fibonacci.py for fibonacci search.

Copyright (C) 2021 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2021 01:10:07 AM EST

DESCRIPTION:
"""
from pydad.datastructure.fibonacci import fibonacci as fib_ds


def fibonacci(seq: list, key: int) -> int:
    len_seq = len(seq)
    # get index of  min element in fibonacci sequence bigger than max element in seq.
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    i = 0
    while True:
        if fib_ds(i) >= len_seq:
            fib_index = i
            break
        i += 1

    offset = 0
    while fib_index > 0:
        middle = min(
            offset + fib_ds(fib_index - 1), len_seq - 1
        )
        middle_value = seq[middle]
        if middle_value == key:
            return middle
        elif key < middle_value:
            fib_index -= 1
        elif key > middle_value:
            offset += fib_ds(fib_index - 1)
            fib_index -= 2
    else:
        return None
        

