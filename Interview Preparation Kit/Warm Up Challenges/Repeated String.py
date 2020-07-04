# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:23:41 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total_a = 0
    len_s = len(s)
    for i in range(len_s):
        if(s[i] == 'a'):
            total_a = total_a + 1
    remain_s = n % len_s
    multiply = n // len_s
    total_a = multiply * total_a
    for i in range(remain_s):
        if(s[i] == 'a'):
            total_a = total_a + 1
    return total_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
