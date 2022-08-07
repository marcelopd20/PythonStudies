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
    def difDiag(arr):
        a, b = 0, 0
        for l in range(len(arr)):
            for c in range(len(arr[l])):
                if l == c:
                    a += arr[l][c]
                if ((l + c) + 1) == len(arr):
                    b += arr[l][c]
        return abs(a - b)
    return difDiag(arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
