# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:43:13 2020

@author: Ashima
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    n = len(a)
    m = len(a[0])
    maxS = INT_MIN = -sys.maxsize-1
    for i in range(n-2):
        for j in range(m-2):
            cur_sum = (a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2])
            if cur_sum > maxS:
                maxS = cur_sum
    return maxS


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
