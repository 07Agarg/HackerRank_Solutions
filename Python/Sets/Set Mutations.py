# Enter your code here. Read input from STDIN. Print output to STDOUT
_, A = int(input()), set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd, _ = input().split()
    B = set(map(int, input().split()))
    if cmd == "intersection_update":
        A.intersection_update(B)
    elif cmd == "update":
        A.update(B)
    elif cmd == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif cmd == "difference_update":
        A.difference_update(B)
print(sum(A))        


