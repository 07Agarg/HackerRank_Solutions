# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
od = OrderedDict()
for _ in range(N):
    key_ = input()
    if od.get(key_):
        od[key_] += 1
    else:
        od[key_] = 1

print(len(od))
for k, v in od.items():
    print(v, end = " ")

#print(*od.values())
