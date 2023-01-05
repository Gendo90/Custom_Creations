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


# finds all combinations possible
# by splitting a number (or string) into composite numbers (groupings of adjacent digits/letters)
# e.g. "123" -> [['1', '2', '3'], ['1', '23'], ['12', '3'], ['123']]
# need to pass in an empty arr variable ([]) or this will not work right (fix later! probably something with arr scope)
def split_comb(s, arr=[]):
    if(len(s) == 0):
        return [""]

    s_arr = [a for a in s]

    new_result = []
    for i in range(1, len(s)+1):
        curr_char = s_arr[:i]
        curr_chars = "".join(curr_char)
        appendations = split_comb("".join(s_arr[i:]), [])
        for ending in appendations:
            curr_mix = [curr_chars] + [*ending]
            new_result.append(curr_mix)
    arr += new_result
    return arr

# gives the full range of combination values as a list
# for a given n (so nC0, nC1, ..., nCn)
# gives the result in O(n) time, with O(n) space
def nCr_table(n):
    output = []

    for i in range(n+1):
        if(i == 0):
            curr_val = 1
        else:
            curr_val = (curr_val) * (n - i + 1) // (i)

        output.append(curr_val)

    return output
