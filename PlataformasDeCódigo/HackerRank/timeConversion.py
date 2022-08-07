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
    if (s[8].lower() == 'a') and s[:2] != '12':
        return s[:8]
    else:
        if s[:2] == '12' and s[8].lower() == 'p':
            return s[:8]
        h = int(s[:2]) + 12
        if h == 24:
            h = '00'
        return f'{h}{s[2:8]}'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()