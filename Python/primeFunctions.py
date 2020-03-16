#!/bin/python3

import math
import os
import random
import re
import sys
import time

def isPrime(n):
    """A prime checker function - determines if n is prime"""

    #special case
    if(n==2):
        return True

    for i in range(2, n//2+1):
        if(n%i==0):
            return False

    return True


def primesToNum(num):
    """Prime number generator function that gives primes up to and
    including the number num"""
    primesList = []

    #special case
    if(num<2):
        return primesList

    for i in range(2, num+1):
        if(isPrime(i)):
            primesList.append(i)

    return primesList

# print(primesToNum(100))
