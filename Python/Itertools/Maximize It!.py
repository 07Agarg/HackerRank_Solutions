# Enter your code here. Read input from STDIN. Print output to STDOUT=
from itertools import product
K, M = map(int, input().split())
square = lambda p: sum((x*x) for x in p)%M
ls1 = []
for _ in range(K):
    ls = list(map(int, input().split()))[1:]
    ls1.append(ls)
s = map(square, product(*ls1))
print(max(s))
