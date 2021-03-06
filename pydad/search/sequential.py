#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sequential.py for search search sequential.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Fri 20 Jan 2017 01:08:39 AM EST

DESCRIPTION:
"""


def sequential(seq, key):
    """Main function for sequential search search.

    :param seq: a sequence.
    :type seq: sequence.
    :param key: an element in the sequence which want to be searched.
    :type key: char or int/float/complex.
    :return index: the index of the key in the seq.
    :rtype index: int.
    """
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return False
