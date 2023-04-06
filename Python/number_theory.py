# gives all palindromes below a given power of 10 (num_digits parameter)
# output is a sorted list of palindromes
def getPalindromesBelow(num_digits):
    output = []

    if(num_digits == 0):
        return output
    if(num_digits == 1):
        return [a for a in range(1, 10)]

    # get all numbers below 10**(num_digits // 2)
    vals = [a for a in range(1, 10**(num_digits // 2))]

    # reflect numbers (reverse) and concatenate with number
    for first_half in vals:
        reverse_val = str(first_half)[::-1]
        # Note that if num_digits is odd, each number must have 0-9 added to the end before concatenation (add loop)
        if(num_digits % 2 == 1):
            for mid_val in range(10):
                curr_val = str(first_half) + str(mid_val) + reverse_val
                output.append(int(curr_val))
        else:
            curr_val = str(first_half) + reverse_val
            output.append(int(curr_val))
    # repeat process for next lower num_digits and add to output array
    output = output + getPalindromesBelow(num_digits - 1)

    # return sorted output array
    return sorted(output)

# gives figurate numbers for triangle numbers upward
# returns the first num_results items in the figurate number series with num_sides (e.g. 3 for triangle, 4 for square, etc.)
def getSeries(num_sides, num_results):
    result_series = [a * ((num_sides - 2) * a + (1 - (num_sides - 3))) // 2 for a in range(1, num_results + 1)]

    return result_series