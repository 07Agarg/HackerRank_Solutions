# Enter your code here. Read input from STDIN. Print output to STDOUT
N, A = input(), set(input().split())
M, B = input(), set(input().split())
print(len(A.difference(B)))