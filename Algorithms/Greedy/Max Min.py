# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:21:02 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    n = len(arr)
    min_diff = sys.maxsize-1
    for i in range(0, n-k+1):
        temp = (arr[k+i-1] - arr[i])
        if temp < min_diff:
            min_diff = temp
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
