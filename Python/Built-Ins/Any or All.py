# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
A = input().split()
print(all([int(a) > 0 for a in A]) and any(x == x[::-1] for x in A))

