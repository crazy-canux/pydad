#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
selection_sort.py for sort algorithm selection.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 01:02:49 AM EST

DESCRIPTION:
"""


def selection_sort(seq):
    """Main function for sort algorithm sort from min to max.

    :param seq: a sequence can be string, tupple, list.
    :type seq: sequence.
    :return seq: return a sequence after sort.
    :rtype seq: sequence.
    """
    for i in range(0, len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[min_index] > seq[j]:
                min_index = j
            if i != min_index:
                seq[i], seq[min_index] = seq[min_index], seq[i]
        return seq
