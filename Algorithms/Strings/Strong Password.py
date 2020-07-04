# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:24:29 2020

@author: Ashima
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    if n == 0:
        return 6
    if n == 1:
        return 5
    if n == 2:
        return 4
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    number_flag = False
    lower_case_flag = False
    upper_case_flag = False
    spec_char = False
    for i in range(n):
        if number_flag and upper_case_flag and lower_case_flag and spec_char:
            if n >= 6:
                return 0
            else:
                return 6 - n
        if password[i] in lower_case:
            lower_case_flag = True
        elif password[i] in upper_case:
            upper_case_flag = True
        elif password[i] in numbers:
            number_flag = True
        elif password[i] in special_characters:
            spec_char = True
    cnt = 0
    if not(number_flag):
        cnt = cnt + 1
    if not(lower_case_flag):
        cnt = cnt + 1
    if not(upper_case_flag):
        cnt = cnt + 1
    if not(spec_char):
        cnt = cnt + 1
    return max(6-n, cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
