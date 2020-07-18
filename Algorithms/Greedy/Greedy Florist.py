# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:18:35 2020

@author: Ashima
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(friends, flowers):
    n = len(flowers)
    if n == friends:
        return sum(flowers)

    flowers.sort()
    total_cost = 0

    j = len(flowers)-1
    loop = n
    while(j >= 0):
        i = 0
        while (i < friends) and (j >= 0):
            total_cost += (1 + (n-loop))*flowers[j]
            i = i + 1
            j = j - 1
        loop = loop - 1
    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
