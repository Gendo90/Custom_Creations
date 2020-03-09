#!/bin/python3

import math
import os
import random
import re
import sys
import time


def reflect(matrix):
    """Takes as input a 2D array, and reflects it about the center column(s)"""
    matrix2 = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[i][len(matrix)-j-1])
        matrix2.append(row)
    return matrix2

def rotate(matrix, t):
    """Rotates a given 2D array 'matrix' the number 't' turns clockwise
    (which can be a negative number)"""
    if(t%4==0):
        return matrix
    elif(t%4==1):
        return rotateOnce(matrix)
    elif(t%4==2):
        matrix2 = rotateOnce(matrix)
        return rotateOnce(matrix2)
    else:
        matrix2 = rotateOnce(matrix)
        matrix3 = rotateOnce(matrix2)
        matrix4 = rotateOnce(matrix3)
        return matrix4


def rotateOnce(matrix):
    """Helper function for 'rotate' above, will rotate a matrix CCW once"""
    rotatedMatrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rotatedMatrix[j].insert(0, matrix[i][j])

    return rotatedMatrix
