# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
S = input()
k = input()
if k in S:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r"(?={})".format(k), S)], sep = "\n")
else:
    print('(-1, -1)')

