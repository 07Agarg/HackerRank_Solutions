# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    _, A = int(input()), set(map(int, input().split()))
    _, B = int(input()), set(map(int, input().split()))
    print(True if len(A.difference(B)) == 0 else False)
