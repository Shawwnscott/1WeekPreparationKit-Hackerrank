#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # Story : Given an array of integers, where all elements but one occur twice, find the unique element.
    # Input : An array of integers
    # Output : Find integer that occurs once
    #### ALGO ####
    # Find the unique values in array using set()
    # Calculate the sum of the unique values
    # Mulitply the sum of unique values by 2
    # Sum the initial array
    # Find the difference between the two
    # That gives the integer that occurs once
   
    sum_arr = sum(set(a))
    sum_a = sum(a)
    result = sum_arr * 2 - sum_a
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
