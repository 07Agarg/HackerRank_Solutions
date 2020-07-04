# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:04:45 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    set1 = set()
    set2 = set()
    for s in s1:
        set1.add(s)
    for s in s2:
        set2.add(s)
    set3 = set1.intersection(set2)
    if len(set3) > 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
