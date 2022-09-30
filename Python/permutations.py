import math
from collections import defaultdict

def getStringPermutations(input, curr_string=""):
    if(input == ""):
        one_val_set = set([curr_string])
        return one_val_set

    input_arr = [a for a in input]
    size = len(input_arr)

    new_result = set()
    for i in range(size):
        curr_char = input_arr.pop(0)
        possible_perms = getStringPermutations("".join(input_arr), curr_string + curr_char)
        for item in possible_perms:
            new_result.add(item)
        input_arr.append(curr_char)


    return new_result

result_set = getStringPermutations("0123456789")

#TODO - rework this to use arrays instead of strings (more common)
