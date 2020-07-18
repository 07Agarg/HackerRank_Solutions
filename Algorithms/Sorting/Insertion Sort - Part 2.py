# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:18:41 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for j in range(1, n):
        k = arr[j]
        i = j - 1
        while arr[i] > k and i >= 0:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = k
        print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
