# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
s = set()
for _ in range(N):
    s.add(input())
#s.add(input() for _ in range(N))        
print(len(s))

