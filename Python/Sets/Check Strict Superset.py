# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())
T = True
for _ in range(N):
    B = set(map(int, input().split()))
    T = T and (len(A) > len(B)) and (B.issubset(A))
print(T)
