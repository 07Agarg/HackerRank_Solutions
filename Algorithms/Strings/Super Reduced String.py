# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:32:38 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(string):
    string_list = list(string)

    flag = True
    while len(string_list) > 0 and flag:
        flag = False
        i = 0
        while i < (len(string_list) - 1):
            if string_list[i] == string_list[i+1]:
                del string_list[i]
                del string_list[i]
                flag = True
            else:
                i = i + 1

    if len(string_list) == 0:
        return "Empty String"
    else:
        s = ""
        for i in range(len(string_list)):
            s += string_list[i]
        return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()