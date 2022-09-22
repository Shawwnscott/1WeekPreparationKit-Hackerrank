#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    ## Algo: 
    ## Change string to ASCII values using for loop and store in temp table.
    ## For each number in range K if Check if ASCII value is UPPER/LOWER then add iteration of K
    ## To Account for end of alphabet - 
    ## Subtracting ASCII at A/a from current ASCII, add K, %26(Numbers of the alphabet), ADD ASCII at A/a
    temp_table = []
    
    for char in s:
        temp_table.append(ord(char))
    
    for i in range(n):
        if 65 <= temp_table[i] <= 90:
            temp_table[i] = (65 + (temp_table[i] - 65 + k)%26)
        elif 97 <= temp_table[i] <= 122:
            temp_table[i] = (97 + (temp_table[i] - 97 + k)%26)
    return "".join(map(chr,temp_table))
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
