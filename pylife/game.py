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

import time

import numpy as np

WRAP = 2


def create(rows, cols, num_states):
    board = np.random.randint(0, num_states, (rows + 2 * WRAP, cols + 2 * WRAP), dtype="uint8")
    core = board[WRAP:-WRAP, WRAP:-WRAP]
    return board, core


def wrap(board):
    board[:WRAP, WRAP:-WRAP] = board[-2 * WRAP:-WRAP, WRAP:-WRAP]
    board[-WRAP:, WRAP:-WRAP] = board[WRAP:2 * WRAP, WRAP:-WRAP]
    board[WRAP:-WRAP, :WRAP] = board[WRAP:-WRAP, -2 * WRAP:-WRAP]
    board[WRAP:-WRAP, -WRAP:] = board[WRAP:-WRAP, WRAP:2 * WRAP]
    board[:WRAP, :WRAP] = board[-2 * WRAP:-WRAP, -2 * WRAP:-WRAP]
    board[:WRAP, -WRAP:] = board[-2 * WRAP:-WRAP, WRAP:2 * WRAP]
    board[-WRAP:, :WRAP] = board[:WRAP, -2 * WRAP:-WRAP]
    board[-WRAP:, -WRAP:] = board[:WRAP, WRAP:2 * WRAP]


def play(rows, cols, states, sensors, rule, fps=25, **kwargs):
    board, core = create(rows, cols, num_states=len(states))
    target_duration = 1 / fps
    actual_duration = 0
    while True:
        start = time.time()
        wrap(board)
        env = sensors(board)
        core[...] = rule[(core,) + env]
        msg = []
        msg.append((rows + 2) * "\033[F")
        for row in core:
            msg.extend(states[val] for val in row)
            msg.append("\n")
        msg.append("\nlongest step: {:.3f}".format(actual_duration))
        print("".join(msg))
        duration = time.time() - start
        actual_duration = max(actual_duration, duration)
        time.sleep(max(0, target_duration - duration))
