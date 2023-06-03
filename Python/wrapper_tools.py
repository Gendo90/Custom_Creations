from itertools import combinations
from functools import reduce
from collections import defaultdict
from time import clock

def time_elapsed(f):
    def fun(*l):
        t0 = clock()
        result = f(*l)
        t1 = clock()

        print("Time elapsed: {} for {}".format(t1-t0, f.__name__))

        return result         
    return fun