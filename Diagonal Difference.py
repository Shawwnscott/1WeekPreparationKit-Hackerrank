#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # Story : Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    # Input : 2D Array of integers
    # Output : Absolute value of an Integer
    # Algo : Loop through array and Figure out the indexes of each integer to be calculated from left to right and right to left.
    
    left_to_right = right_to_left = 0
    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n-1-i]
    return abs(left_to_right- right_to_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
