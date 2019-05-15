# Enter your code here. Read input from STDIN. Print output to STDOUT
K, A = int(input()), list(map(int, input().split()))
B = set(A)
print((sum(B) * K  - sum(A))//(K - 1))




