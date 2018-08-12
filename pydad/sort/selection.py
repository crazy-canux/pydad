#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
selection.py for sort search selection.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Wed 18 Jan 2017 01:02:49 AM EST

DESCRIPTION:
"""


def selection_sort(seq):
    """Main function for sort search sort from min to max.

    :param seq: a sequence can be string, tupple, list.
    :type seq: sequence.
    :return seq: return a sequence after sort.
    :rtype seq: sequence.
    """
    for i in range(len(seq)-1):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]
    return seq
