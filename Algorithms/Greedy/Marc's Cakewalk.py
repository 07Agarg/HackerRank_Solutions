# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:53:22 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    n = len(calorie)
    ans = 0
    for i in range(n-1, -1, -1):
        ans = ans + pow(2, i) * calorie[i]
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
