#!/usr/bin/env python3
"""
SUMMARY fibonacci.py

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 17 May 2017 10:21:34 AM EDT

DESCRIPTION:
    f(0) = 0
    f(1) = 1
    f(n) = f(n-2) + f(n-1) (n>=2)
"""


def fibonacci_list(index):
    fib_list = [0, 1]
    for _ in range(index-1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[index]


def fibonacci(index):
    if index < 0:
         exit(0)
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)


if __name__ == "__main__":
    print(fibonacci_list(0))
    print(fibonacci_list(1))
    print(fibonacci_list(2))
    print(fibonacci_list(3))
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))