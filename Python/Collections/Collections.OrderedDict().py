# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
od = OrderedDict()
for _ in range(N):
    line = input().split()
    item_name, item_price = ' '.join(line[:-1]), int(line[-1])
    if od.get(item_name):
        od[item_name] += item_price
    else:
        od[item_name] = item_price
        
for k,v in od.items():
    print(k, v)
