#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #story: Given 5 positive integers, find the min an max values that can be calculated by summing exactly four of the 5 integers
    #Inputs: 5 positive integers
    #Output: Minimum and Maximum Values
    #Algo: 
    # Step 1. Loop through array to get maximum and minimum number in array 
    # Step 2. Subtract the max and min number from the sum of array 
    #Step 3. Print each
    total = 0 
    minnum = 989898989
    maxnum = 0 
    num = len(arr)
    for i in range (num):
        total += arr[i]
        minnum = min(minnum, arr[i])
        maxnum = max(maxnum, arr[i])
    print(total- maxnum, total- minnum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
