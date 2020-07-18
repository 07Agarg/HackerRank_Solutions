# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:12:44 2020

@author: Ashima
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def partition(arr):
    pivot = arr[0]
    pivot_index = 0
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            j = i;
            while(j > pivot_index):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j = j - 1
            pivot_index = pivot_index + 1 
    return pivot_index


def quickSort(arr):
    if (len(arr) > 1):
        index = partition(arr)
        a1 = quickSort(arr[:(index)])
        a2 = quickSort(arr[(index+1):])
        arr = a1 + [arr[index]] + a2
        print(*arr)
    return arr


n = int(input())
arr = list(map(int, input().rstrip().split()))
result = quickSort(arr)