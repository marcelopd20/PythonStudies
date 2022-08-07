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
    a,b,c = 0,0,0
    for x in arr:
        if x > 0:
            a += 1
        elif x == 0:
            b += 1
        else:
            c += 1
    return f'{a/len(arr):.6f}\n{c/len(arr):.6f}\n{b/len(arr):.6f}'

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
    print(n)
