#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

def get_fib_value_while(number):
    index = 0
    pre, nxt = 0, 1
    while index < number:
        pre, nxt = nxt, pre + nxt
        index += 1
    return pre

def get_fib_value_recursion(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return get_fib_value_recursion(number-2) + \
            get_fib_value_recursion(number-1)

def get_fib_value_iter(number):
    fib_list = [0, 1]
    for _ in range(number-1):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list[number]

def get_fib_sum_while(number):
    index = 0
    fsum = 0
    pre, nxt = 0, 1
    while index < number:
        pre, nxt = nxt, pre + nxt
        fsum += pre
        index += 1
    return fsum

if __name__ == "__main__":
    for loop in range(10):
        print get_fib_value_while(loop)
        print get_fib_value_recursion(loop)
        print get_fib_value_iter(loop)
        print 'sum: ', get_fib_sum_while(loop)
