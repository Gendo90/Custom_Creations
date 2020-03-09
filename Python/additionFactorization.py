#!/bin/python3

import math
import os
import random
import re
import sys
import time

#Note - originally used to try to tackle the Magic Squares problem, since
#numbers on the diagonals need to work for 3 sets (diagonal, row, and column),
#the center number must work for all sets (if there is a center),
#and all other numbers need to work for 2 sets (row and column), but this
#seems to have some use on Project Euler as well, so I am saving it in
#Custom Creations!
def recursiveSums(desiredNum, values, depth=0, max_depth=5):
    """
    Recursive function to determine all valid combinations of numbers in
    the 'values' array that sum to the 'desiredNum' target number.

    This is a combinatoric function that essentially checks combinations of
    values from the array 'values' to see if they sum to the 'desiredNum', so
    some changes have been made to only see each combination of values once to
    improve the algorithmic running time. Since this is an O(n!) combinatoric
    function, the running time grows rapidly with respect to n (which
    represents the size of the list of values) but it can also run quickly if
    there are few or no possible solutions.

    This function will run up to the recursive depth set by max_depth, so if
    this value is set to 5, there will be at most 5 numbers used in a set of
    numbers that sums to the desiredNum, and no more. There can be fewer
    numbers used in any set, however.

    Parameters:
    desiredNum: A number that is the target value of the summation of
    combinations of the numbers in the 'values' parameter

    values: An array of numbers that represent the set of numbers available to
    sum to the 'desiredNum' target value (the 'addition factors')

    depth: a reference value to compare to the number of recursive calls -
    does not need to be changed from 0!

    max_depth: a number that represents the maximum size of the set of numbers
    to be summed - e.g. if you only want 5 factors or fewer, set it to 5

    Returns:
    arr: An array of nested arrays that needs to be post-processed by
    'convertSumsToMap' which uses a helper function 'setFromValues' to
    recursively decompose the nested arrays output by this function into
    a partially-complete map of all the combinations (not including duplicate
    values, so each set of numbers is only seen once in this map)
    """
    depth+=1
    if(depth>max_depth):
        return
    if(len(values)==1):
        if(values[0]==desiredNum):
            return values[0]
    else:
        arr = []
        removals = []
        for i, value in enumerate(values):
            thisDesiredNum = desiredNum-value
            if(thisDesiredNum==0):
                arr.append(value)
            elif(thisDesiredNum>0):
                #quick fix prevents double counting here
                newValues = [l for l in values if(l not in removals)]
                newValues.pop(newValues.index(value))
                arr.append([value])
                if(len(newValues)!=0 and sum(newValues)>=thisDesiredNum):
                    newSums = recursiveSums(thisDesiredNum, newValues, depth, max_depth)
                    if(newSums):
                        if(isinstance(newSums, int)):
                            arr.append([newSums])
                        else:
                            arr[-1].extend(newSums)
                        if(len(arr[-1])==0 or arr[-1]==[value]):
                            arr.pop()
            removals.append(value)
        #remove unusable values
        iteratedValues = [value for value in values if(value not in removals)]
        if(iteratedValues):
            arr.append(recursiveSums(desiredNum, iteratedValues, depth, max_depth))
        return arr

def convertSumsToMap(arr, values):
    """
    Creates a map from the output of 'recursiveSums' with the numbers in
    its parameter 'values' as the keys, using the helper function
    'setFromValues'
    """
    num_map = {}
    for item in values:
        num_map[item] = []

    for i in range(len(arr)):
        num_map[i+1] = setFromValues(arr[i])

    return num_map

#recursively gather up the nested arrays into sets
def setFromValues(arr):
    """
    Helper function for 'convertSumsToMap', this function takes in an
    array for a specific number in the set of 'values' and recursively converts
    it to an array that contains all the sets of numbers summing to the
    'desiredNum' value including that number
    """
    if(isinstance(arr, int)):
        return arr
    num = arr.pop(0)
    currSet = set()
    currSet.add(num)
    allSets = [currSet]
    for i in range(len(arr)):
        if(isinstance(arr[i], int)):
            currSet.add(arr[i])
        else:
            newSet = set()
            newSet.add(num)
            nestedSets = setFromValues(arr[i])
            for a in nestedSets:
                newSet = newSet.union(a)
                if(newSet not in allSets):
                    allSets.append(newSet)
                newSet = set()
                newSet.add(num)
    #case where there are no matches for the first item
    if(len(allSets[0])==1):
        allSets.pop(0)
    return allSets

#add sets for larger values contained in sets that do not map to the set
#already due to the restrictions on the algorithm additive factor search to
#speed up the algorithm
def completeMap(partialMapArr, setLen=-1):
    """
    Final post-processing step that takes in the output of
    'convertSumsToMap' and creates an updated map with all sets containing a
    number accessible given that number as the key

    Parameters:
    partialMapArr: output map from 'convertSumsToMap' - this contains no
    duplicate sets, so they need to be duplicated so that each number
    maps to ALL sets containing it that sum to the target value

    setLen: a number that represents the desired length of all the sets
    included in the final mapping of values to sets of values. This is set to
    -1 by default to include sets of any size, but can be set to 2 for example
    if you only want valid combinations of numbers that contain two numbers, no
    more and no less! This should be used in tandem with the 'max_depth'
    parameter in the 'recursiveSums' function to filter out valid combinations
    of numbers that sum to the 'desiredNum' but do not use the desired amount
    of values to form the combination!
    """
    a = time.clock()
    fullMap = partialMapArr.copy()
    count = 0
    seen = {}
    for key in partialMapArr.keys():
        thisNumSets = partialMapArr[key]
        removals = []
        for i, setItem in enumerate(thisNumSets):
            tupleVersion = tuple(list(setItem))
            if(tupleVersion in seen):
                break
            else:
                seen[tupleVersion] = True
            #conditional to filter out all sets that are not a certain length
            if(len(setItem)==setLen or setLen==-1):
                for num in setItem:
                    count+=1
                    if(num==key):
                        continue
                    if(setItem not in fullMap[num]):
                        fullMap[num].append(setItem)
            else:
                removals.append(i)
        removals.reverse()
        for item in removals: thisNumSets.pop(item)
    b = time.clock()

    #returns the map with duplicated values, the number of values seen (n for
    #O(n)), and the time elapsed to run the function
    return fullMap, count, (b-a)


a = [i for i in range(1, 10)]

n = recursiveSums(15, a, depth=0, max_depth=3)

partialMap = convertSumsToMap(n, a)
# print(partialMap)
print(completeMap(partialMap))
