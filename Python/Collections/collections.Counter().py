# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
X, A = int(input()), collections.Counter(map(int, input().split()))
N = int(input())
money = 0
for _ in range(N):
    z, price = map(int, input().split())
    if A[z]:
        money += price
        A[z] -= 1
print(money)
