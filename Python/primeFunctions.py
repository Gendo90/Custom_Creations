#!/bin/python3

import math
import os
import random
import re
import sys
import time

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

def isPrimeUpgraded(n):
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

    for i in range(2, int(math.sqrt(n))+2):
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
        if(isPrimeUpgraded(i)):
            primesList.append(i)

    return primesList

# print(len(primesToNum(1000000)))
