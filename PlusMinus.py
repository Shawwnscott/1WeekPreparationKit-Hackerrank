#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #Story: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
    #Inputs: Array of integers
    #Outputs: Ratios of its elements that are positive, negative, and zero
    #Algo: Loop through array.Count the total Positive, negative and zero values. Calculate Ratio of each (sum of count / count of total). 
    #Constraints : Round up to 6 decimal places.
    pos = neg = zero = 0 
    for i in range(n):
        if arr[i] > 0:
            pos +=1
        elif arr[i]< 0:
            neg += 1
        else:
            zero += 1
    # Use format specifier to maintain decimal places     
    print(f"{pos/len(arr):.6f}")
    print(f"{neg/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")
    # Use format specifier to maintain decimal places        
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
