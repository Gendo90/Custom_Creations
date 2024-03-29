import math

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


# use Extended Euclidean Algorithm: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# keep track of quotients for each value compared and not just remainders!
# gives the mod multiplicative inverse
def mod_mult_inv(a, m):
    # coprime condition for mod inverse to exist
    if (not math.gcd(a, m) == 1):
        return -1

    # reduce a if larger to m to its congruence below m
    a = a % m

    steps = [[m, 1, 0], [a, 0, 1]]

    while (not steps[-1][0] == 1):
        # g > h as a rule
        g, h = steps[-2][0], steps[-1][0]
        q, r = divmod(g, h)

        steps.append([r, steps[-2][1] - q * steps[-1][1],
                     steps[-2][2] - q * steps[-1][2]])

    return steps[-1][-1] % m


# returns (a**b) % m quickly!
# use exponentiation shortcut from lecture/number theory notes
def fast_exp(a: int, b: int, m: int) -> int:
    if (a == 0):
        return 0

    # convert to binary string, reversed for easier iteration
    rev_bin_b = bin(b)[2:][::-1]

    # calc array of values for a ** (2**k) % m for quick exponentiation
    # start with 2**0 = 1 so a**1 => a
    arr = [a]
    for i in range(len(rev_bin_b) - 1):
        last_val = arr[-1]
        arr.append((last_val**2) % m)

    result = 1
    for i, val in enumerate(rev_bin_b):
        if (val == "1"):
            result *= arr[i]
            result %= m

    return result
