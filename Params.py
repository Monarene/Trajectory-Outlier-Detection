#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:14:35 2020

@author: michael
"""

#skipping all the definitions and applying the constant
g_FRACTION_PARAMETER = 0.95
g_DISTANCE_PARAMETER = 82.0
g_MINIMUM_OUTLYING_PROPORTION = 0.50
MDL_COST_ADVANTAGE = 20
MIN_LINSEGMENT_LENGTH = 1.0
MAX_LINESEGMENT_LENGTH = 10000.0

def WEIGHTED_DISTANCE(x, y, z):
    return (1.0 * x + 1.0 * y + 10.0 * z)

RESULT_FILE = "results.txt"