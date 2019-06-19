# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
num_list = input().split()
k = int(input())
t = list(combinations(num_list, k))
f = [i for i in t if 'a' in i]
print(len(f)/len(t))
