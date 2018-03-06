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


def rule_to_name(rule):
    return ".".join("".join(str(x) for x in row.flatten()) for row in rule)


def name_to_rule(name, shape=None):
    res = np.array([[int(char) for char in part] for part in name.split(".")])
    if shape is not None:
        res = res.reshape(shape)
    return res


def random_rules(shape):
    num_states = shape[0]
    while True:
        yield np.random.randint(0, num_states, shape, dtype="uint8")


def all_rules(shape):
    num_states = shape[0]
    num_values = np.prod(shape[1:])
    while True:
        for x in range(2 ** (num_states * num_values)):
            binary_str = "{{:0{}b}}".format(num_states * num_values).format(x)
            name = ".".join(binary_str[i * num_values:(i + 1) * num_values] for i in range(num_states))
            yield name_to_rule(name, shape)
