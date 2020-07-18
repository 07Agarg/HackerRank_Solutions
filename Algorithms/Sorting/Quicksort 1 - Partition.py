# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:52:33 2020

@author: Ashima
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            j = i;
            while(j > 0):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j = j -1
    return(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
