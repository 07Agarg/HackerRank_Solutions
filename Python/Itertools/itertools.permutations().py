# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
A, B = input().split()
print(*[''.join(i) for i in permutations(sorted(A), int(B))], sep = '\n')
