# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:13:08 2020

@author: Ashima
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridChallenge function below.
def gridChallenge(grid):
    #print(grid)
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        s = list(grid[i])
        s.sort()
        s_new = ''.join(map(str, s))
        result.append(s_new)

    for i in range(m):
        for j in range(n-1):
            if result[j][i] > result[j+1][i]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
