# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
A, B = input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(A), int(B))], sep = "\n")
