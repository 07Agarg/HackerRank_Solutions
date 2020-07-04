# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:26:35 2020

@author: Ashima
"""
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)
    d1 = n - d
    result = [None]*n
    for i in range(n):
        index = (i + d1)%n
        result[index] = a[i]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
