#!/usr/bin/env python3
"""
two number sum is target
"""
from typing import List

def sum(seq: List[int], target: int) -> List[int]:
    for i in range(len(seq)-1):
        for j in range(i+1, len(seq)):
            if seq[i] + seq[j] == target:
                return i, j
    return -1, -1

def sum_v1(seq: List[int], target: int) -> List[int]:
    for i in range(len(seq)-1):
        rest = target - seq[i]
        if rest in seq[i+1:]:
            return i, seq[i+1:].index(rest)+i+1
    return -1,-1


if __name__ == "__main__":
    print(sum([1,2,4,6,8], 10))
    print(sum_v1([1,2,4,6,8], 10))