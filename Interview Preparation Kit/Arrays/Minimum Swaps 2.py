# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:56:57 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    visited_map = [False]*n
    total_len = 0
    for i in range(n):
        if visited_map[i] == False:
            visited_map[i] = True
            length = 1
            b = arr[i] - 1
            while b != i:
                visited_map[b] = True
                length = length + 1
                b = arr[b] - 1
            total_len += (length - 1)
    return total_len



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
