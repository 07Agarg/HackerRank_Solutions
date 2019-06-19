# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lower = []
upper = []
odd = []
even = []
for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif int(i) % 2 != 0:
        odd.append(int(i))
    elif int(i) % 2 == 0:
        even.append(int(i))

lower.sort()
upper.sort()
odd.sort()
odd = list(map(str, odd))
even.sort()
even = list(map(str, even))
final = lower + upper + odd + even
print(*final, sep = '')


