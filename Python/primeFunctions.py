#!/bin/python3

import math
import os
import random
import re
import sys
import time
from collections import defaultdict

def isPrime(n):
    """A prime checker function - determines if n is prime in O(n) time"""

    #special cases
    if(n==2):
        return True
    if(n<2):
        return False

    for i in range(2, n//2+1):
        if(n%i==0):
            return False

    return True

def isPrimeUpgraded(n, start_val=2):
    """A prime checker function - determines if n is prime faster O(sqrt(n))
    time"""

    #extension to work for non-integer values (which are never prime)
    if(not isinstance(n, int)):
        return False

    #special cases
    if(n==2):
        return True
    if(n<2):
        return False

    for i in range(start_val, int(math.sqrt(n))+2):
        if(n%i==0):
            return False

    return True


#stress test of isPrimeUpgraded
# n = 0
# while(isPrimeUpgraded(n)==isPrime(n)):
#     print(isPrime(n), isPrimeUpgraded(n), n)
#     n+=1
# else:
#     print("error on n=", n)

#returns if a number is prime or not!
def primesToNum(num):
    """Prime number generator function that gives primes up to and
    including the number num"""
    primesList = []

    #special case
    if(num<2):
        return primesList

    for i in range(2, num+1):
        # print(i)
        if(isPrimeUpgraded(i)):
            primesList.append(i)

    return primesList

print(len(primesToNum(32000)))

# creates a list of all primes up to a specified number
# uses memoization and recursion
# does not work for large values due to recursion limit in Python
def getAllPrimesBelowNum(num, curr_num=2, primesList=[]):
    print(curr_num)
    # also accounts of num < 2
    if(curr_num > num):
        return primesList

    #ensure the list is always populated
    if(curr_num == 2):
        return getAllPrimesBelowNum(num, 3, [2])

    # start with the last value of primesList
    # if number not factorized
    for prime in primesList:
        if(curr_num % prime == 0):
            # not a prime number, skip to next curr_num
            return getAllPrimesBelowNum(num, curr_num+1, primesList)
    #otherwise, start with last number plus 1 for primesList
    start_val = primesList[-1] + 1

    # now run the isPrimeUpgraded with a custom start value of curr_num
    if(isPrimeUpgraded(curr_num, start_val)):
        primesList.append(curr_num)

    return getAllPrimesBelowNum(num, curr_num + 1, primesList)

# sys.setrecursionlimit(1000000000)
#
# print(getAllPrimesBelowNum(10000))


def getAllPrimesBelowNumUpgraded(num, primesList=[]):
    time.clock()
    if(num < 2):
        return primesList

    # initialize primes list with 2
    primesList.append(2)

    curr_num = 3

    while(num >= curr_num):
        # print(curr_num)
        orig_curr_num = curr_num
        # check if curr_num is divisible by a previously found prime
        # do not need to check other numbers due to prime factorization
        for prime in primesList:
            if(curr_num % prime == 0):
                # not a prime number, skip to next curr_num
                curr_num += 1
                break
        if(not orig_curr_num == curr_num):
            continue
        #otherwise, start with last number plus 1 for primesList
        start_val = primesList[-1] + 1

        #check if curr_num is prime
        if(isPrimeUpgraded(curr_num, start_val)):
            primesList.append(curr_num)

        curr_num += 1

    print("Time elapsed: {}".format(time.clock()))
    print(len(primesList))

    return primesList

# getAllPrimesBelowNumUpgraded(int(math.sqrt(10**9) + 2))
# getAllPrimesBelowNumUpgraded(int(math.sqrt(2147483647) + 2))
# getAllPrimesBelowNumUpgraded(10**6)


# to get prime factors for a number n
# note that there is some pre-processing that can be
# moved outside the function in case there is a consistent upper limit
# for a problem with multiple testcases
def primeFactors(num, primesList=[]):
    # pre-processing to be moved outside the function
    # in case the primesList is already calculated
    if(len(primesList) == 0):
        primesList = primesToNum(num)

    # if primesList already calculated, skip to prime factorization here:
    factors = defaultdict(int)
    ind = 0
    while(num > 1):
        # update primeList if the existing primeList does not include a high enough prime - to be added later
        # right now, just check if the number is prime
        if(ind >= len(primesList)-1):
            if(isPrimeUpgraded(num)):
                factors[int(num)] += 1
                break

        curr_prime = primesList[ind]
        # divide out the current prime until it is no longer present,
        # counting the number of times factored out
        while(num / curr_prime == num // curr_prime):
            factors[curr_prime] += 1
            num /= curr_prime

        ind += 1

    return factors
# print(primeFactors(63982))
# print(primeFactors(10000000))

# print(isPrimeUpgraded(65837))


# use sieve of erastothenes algorithm to find primes in a given range, n to m inclusive
# - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity
# much quicker than trial division due to every number multiple being used and no "misses" when dividing primes
# with a memoized primeList that must be calculated up to the ceil(sqrt(m))
# e.g. primesList = primesToNum(int(math.sqrt(m) + 2))
def erastosthenesSieve(n, m, primeList):
    arr = [a for a in range(n, m+1) if (a % 2 == 1 and not a == 1)]
    range_primes = set(arr)

    # print(primesList)

    for prime in primesList:
        if(prime == 2):
            continue
        lower_bound = n // prime
        upper_bound = m // prime
        for removal in range(lower_bound, upper_bound+1):
            # case where it is the prime itself
            if (removal == 1):
                continue
            range_primes.discard(removal*prime)

    output = list(range_primes)
    output.sort()

    return output

# erastosthenes sieve with prime factor set for each non-prime number, stored in a map
# starting from 2 upward to n
def erastothenesSieveFactors(n):
    primes_set = set()
    seen = set()
    prime_factor_map = defaultdict(list)

    for i in range(2, n+1):
        if(i not in seen):
            primes_set.add(i)
            for j in range(i, n+1, i):
                prime_factor_map[j].append(i)
                seen.add(j)
    return primes_set, prime_factor_map


# prime factors as a defaultdict of primes to count of those primes
def erastothenesSieveFactorsCount(n):
    primes_set = set()
    seen = set()
    prime_factor_map = defaultdict(lambda: defaultdict(int))

    for i in range(2, n+1):
        if(i not in seen):
            primes_set.add(i)
            for j in range(i, n+1, i):
                j2 = j
                while(j2 % i == 0):
                    prime_factor_map[j][i] += 1
                    j2 /= i
                seen.add(j)
    return primes_set, prime_factor_map
