n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    p = input().split()
    if p[0] == "pop":
        s.pop()
    elif p[0] == "remove":
        s.remove(int(p[1]))
    else:
        s.discard(int(p[1]))
print(sum(s))

