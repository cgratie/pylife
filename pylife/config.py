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

import json

import numpy as np

from . import environment
from . import squares


def load(path):
    with open(path, "rt") as in_file:
        params = json.load(in_file)

    if params["display_mode"] == "squares":
        params["states"] = [squares.get(state) for state in params["states"]]
    else:  # "plain"
        pass

    params["sensors"] = environment.get(params["sensors"])

    rule = np.zeros((len(params["states"]),) + tuple(params["rule_shape"]), dtype="uint8")
    for in_state, in_data in enumerate(params["rule"]):
        for out_state, out_data in enumerate(in_data):
            for indices in out_data:
                rule[(in_state,) + tuple(indices)] = out_state + 1
    params["rule"] = rule

    return params
