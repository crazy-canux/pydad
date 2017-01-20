#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
min_max.py get the min or max value from a sequence.

Copyright (C) 2017 Canux CHENG.
All rights reserved.

LICENSE GNU General Public License v3.0.

:author: Canux CHENG canuxcheng@gmail.com
:version: V1.0.0.0
:since: Thu 19 Jan 2017 11:45:16 PM EST

DESCRIPTION:
"""


def min(seq):
    """Main function used to find the min value from a sequence.

    :param seq: the sequence include string, tupple, list.
    :type seq: sequence.
    :return min: return the min value in the seq.
    :rtype min: string
    """
    min = seq[0]
    for i in range(1, len(seq)):
        if min > seq[i]:
            min = seq[i]
    return min


def max(seq):
    """Main function used to find the max value from a sequence.

    :param seq: the sequence include string, tupple, list.
    :type seq: sequence.
    :return max: return the max value in the seq.
    :rtype max: string
    """
    max = seq[0]
    for i in range(1, len(seq)):
        if max < seq[i]:
            max = seq[i]
    return max


if __name__ == "__main__":
    seq = [198, 25, -7, 27, 0, 25, 87]
    print("original seq: {}".format(seq))
    print("min: {}".format(min(seq)))
    print("max: {}".format(max(seq)))

    seq = (198, 25, -7, 27, 0, 25, 87)
    print("original seq: {}".format(seq))
    print("min: {}".format(min(seq)))
    print("max: {}".format(max(seq)))

    seq = "sdogiahgosnhlazsbndohasdnhklansdh"
    print("original seq: {}".format(seq))
    print("min: {}".format(min(seq)))
    print("max: {}".format(max(seq)))
