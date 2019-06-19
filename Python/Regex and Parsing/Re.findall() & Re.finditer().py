# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])", input())
if m:
    print(*m, sep = '\n')
else:
    print('-1')
