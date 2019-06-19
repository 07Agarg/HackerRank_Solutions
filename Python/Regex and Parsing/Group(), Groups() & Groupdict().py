# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.search(r"([0-9A-Za-z])\1+", input())
print(m.group(1) if m else -1)

