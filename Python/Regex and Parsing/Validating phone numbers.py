# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    s = input()
    if re.match(r"[789]\d{9}$", s):
        print("YES")
    else:
        print("NO")
