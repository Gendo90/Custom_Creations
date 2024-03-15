# uses binary search to find the nth roots of an integer
# TODO:
# only returns integers right now, can be extended for any number of digits later (add a parameter for number of digits)
# may convert to an integer with trailing zeros (multiply by power of 10) to get decimal precision, 
# then divide by same power of 10
def find_root(N, r_num):
    # only valid for positive integer N
    if (N < 1):
        return -1

    min, max = 0, N
    mid = (min + max) // 2
    calc_val = int(mid**r_num)

    while (not calc_val == N):
        if (calc_val <= N):
            min = mid
        else:
            max = mid
        mid = (min + max) // 2
        calc_val = int(mid**r_num)

    return mid
