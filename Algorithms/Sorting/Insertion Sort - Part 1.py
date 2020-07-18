# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:09:54 2020

@author: Ashima
"""


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    k = arr[n-1]
    i = n-2
    while arr[i] > k and i >= 0:
        arr[i+1] = arr[i]
        i = i - 1
        print(*arr)
    arr[i+1] = k
    print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
