#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for c in range(n):
        print(' '*abs(c-n+1), '#'*(c+1), sep='')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)