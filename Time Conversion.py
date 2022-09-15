#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # Story: Given a time in 12 Hour format convert to 2 hour
    # Inputs: Time in PM/AM
    # Output: Military Time
    # Hint utilize slicing on array.
    ##### Algo ####
    # Slice AM/PM from string.
    # If PM and First two index != 12 (If after 12 o clock)
    # Then Calculate new time by adding the current hour to 12
    # IF AM and First two index == 12 then change the first indexes to '00'
    
    meridem  = s[-2:]
    if meridem == 'PM' and s[:2] != '12':
        s = str( 12 + int(s[:2])) + s[2:]
    if meridem == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
