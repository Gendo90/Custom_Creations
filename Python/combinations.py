#!/bin/python3

import math
import os
import random
import re
import sys


# takes a string "s" and returns all possible combinations
# n C r for r -> 1 to len(s)
# in lexicographic order
def solve(s):
    # sort s so alphabetically in order as index increases
    combinations = set('')

    combinations = find_comb_improved(s, combinations).copy()

    combinations.discard('')
    output = list(combinations)
    output.sort()

    return output



def find_comb_improved(s, seen=set('')):
    s_arr = [a for a in s]

    result_set = seen.copy()

    for item in s_arr:
        for existing_item in seen:
            result_set.add(existing_item + item)
        result_set.add(item)
        seen = result_set.copy()

    return seen


# gives the full range of combination values as a list
# for a given n (so nC0, nC1, ..., nCn)
def nCr_table(n):
    output = []

    for i in range(n+1):
        if(i == 0):
            curr_val = 1
        else:
            curr_val = (curr_val) * (n - i + 1) // (i)

        output.append(curr_val)

    return output
