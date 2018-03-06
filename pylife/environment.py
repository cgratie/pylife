# -*- coding: utf-8 -*-

# pylife
# 
# Copyright (c) 2018 Cristian Gratie
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

from __future__ import absolute_import, division, print_function
from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

import numpy as np

from .game import WRAP


def n4binary(board):
    res = np.zeros_like(board[WRAP:-WRAP, WRAP:-WRAP], dtype="uint8")
    res += board[WRAP:-WRAP, WRAP - 1:-WRAP - 1] > 0
    res += board[WRAP:-WRAP, WRAP + 1:-WRAP + 1] > 0
    res += board[WRAP - 1:-WRAP - 1, WRAP:-WRAP] > 0
    res += board[WRAP + 1:-WRAP + 1, WRAP:-WRAP] > 0
    return res,


def n4multistate(num_states):
    def sensors(board):
        results = []
        for val in range(1, num_states):
            res = np.zeros_like(board[WRAP:-WRAP, WRAP:-WRAP], dtype="uint8")
            res += board[WRAP:-WRAP, WRAP - 1:-WRAP - 1] == val
            res += board[WRAP:-WRAP, WRAP + 1:-WRAP + 1] == val
            res += board[WRAP - 1:-WRAP - 1, WRAP:-WRAP] == val
            res += board[WRAP + 1:-WRAP + 1, WRAP:-WRAP] == val
            results.append(res)
        return tuple(results)

    return sensors


def n8binary(board):
    res = np.zeros_like(board[WRAP:-WRAP, WRAP:-WRAP], dtype="uint8")
    res += board[WRAP - 1:-WRAP - 1, WRAP - 1:-WRAP - 1] > 0
    res += board[WRAP - 1:-WRAP - 1, WRAP:-WRAP] > 0
    res += board[WRAP - 1:-WRAP - 1, WRAP + 1:-WRAP + 1] > 0
    res += board[WRAP:-WRAP, WRAP - 1:-WRAP - 1] > 0
    res += board[WRAP:-WRAP, WRAP + 1:-WRAP + 1] > 0
    res += board[WRAP + 1:-WRAP + 1, WRAP - 1:-WRAP - 1] > 0
    res += board[WRAP + 1:-WRAP + 1, WRAP:-WRAP] > 0
    res += board[WRAP + 1:-WRAP + 1, WRAP + 1:-WRAP + 1] > 0
    return res,


def n8multistate(num_states):
    def sensors(board):
        results = []
        for val in range(1, num_states):
            res = np.zeros_like(board[WRAP:-WRAP, WRAP:-WRAP], dtype="uint8")
            res += board[WRAP - 1:-WRAP - 1, WRAP - 1:-WRAP - 1] == val
            res += board[WRAP - 1:-WRAP - 1, WRAP:-WRAP] == val
            res += board[WRAP - 1:-WRAP - 1, WRAP + 1:-WRAP + 1] == val
            res += board[WRAP:-WRAP, WRAP - 1:-WRAP - 1] == val
            res += board[WRAP:-WRAP, WRAP + 1:-WRAP + 1] == val
            res += board[WRAP + 1:-WRAP + 1, WRAP - 1:-WRAP - 1] == val
            res += board[WRAP + 1:-WRAP + 1, WRAP:-WRAP] == val
            res += board[WRAP + 1:-WRAP + 1, WRAP + 1:-WRAP + 1] == val
            results.append(res)
        return tuple(results)

    return sensors


def get(identifier):
    return globals()[identifier]
