# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:30:11 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the runningTime function below.
def runningTime(arr):
    shifts = 0
    for j in range(1, n):
        k = arr[j]
        i = j - 1
        while arr[i] > k and i >= 0:
            arr[i+1] = arr[i]
            i = i - 1
            shifts = shifts + 1
        arr[i+1] = k
    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
