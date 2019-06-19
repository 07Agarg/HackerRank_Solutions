# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
s = input()
length = len(s)
i = 0
while(i < len(s)):
    X = 1
    char = s[i]
    j = i + 1
    while(j < len(s) and char == s[j]):
        X += 1
        j += 1
    print((X, int(char)), end = " ")
    i = j
"""
from itertools import groupby
#print(*[(k, *list(c)) for k, c in groupby(input())])
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
