# -*- coding: utf-8 -*-
"""Merged real-type diagram set (equipment/process style) for DI04005071."""
from diagrams_r1 import D as _D1
from diagrams_r2 import D as _D2
from diagrams_r3 import D as _D3

REAL = {}
for _d in (_D1, _D2, _D3):
    REAL.update(_d)
