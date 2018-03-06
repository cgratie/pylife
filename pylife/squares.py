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

_square = u"\u2B1B"
_color = {
    "black": u"\u001b[30m",
    "red": u"\u001b[31m",
    "green": u"\u001b[32m",
    "yellow": u"\u001b[33m",
    "blue": u"\u001b[34m",
    "magenta": u"\u001b[35m",
    "cyan": u"\u001b[36m",
    "white": u"",
}
_bright = lambda color: color[:-1] + u";1m"
_reset = u"\u001b[0m"

BLACK = _color["black"] + _square + _reset + " "
WHITE = _color["white"] + _square + _reset + " "
RED = _color["red"] + _square + _reset + " "
GREEN = _color["green"] + _square + _reset + " "
BLUE = _color["blue"] + _square + _reset + " "
CYAN = _color["cyan"] + _square + _reset + " "
MAGENTA = _color["magenta"] + _square + _reset + " "
YELLOW = _color["yellow"] + _square + _reset + " "

BRIGHT_BLACK = _bright(_color["black"]) + _square + _reset + " "
BRIGHT_WHITE = _bright(_color["white"]) + _square + _reset + " "
BRIGHT_RED = _bright(_color["red"]) + _square + _reset + " "
BRIGHT_GREEN = _bright(_color["green"]) + _square + _reset + " "
BRIGHT_BLUE = _bright(_color["blue"]) + _square + _reset + " "
BRIGHT_CYAN = _bright(_color["cyan"]) + _square + _reset + " "
BRIGHT_MAGENTA = _bright(_color["magenta"]) + _square + _reset + " "
BRIGHT_YELLOW = _bright(_color["yellow"]) + _square + _reset + " "


def get(identifier):
    return globals()[identifier]
