# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    p = input()
    if p in d:
        print(' '.join(map(str, d[p])))
    else:
        print(-1)
