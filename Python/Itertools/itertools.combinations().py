# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
A, B = input().split()
print(*[''.join(i) for j in range(1, int(B) + 1) for i in combinations(sorted(A), j)], sep ="\n")
