# Enter your code here. Read input from STDIN. Print output to STDOUT
M, A = int(input()), set(map(int, input().split()))
N, B = int(input()), set(map(int, input().split()))
#print(*sorted(list(A.symmetric_difference(B))), sep = '\n')
print('\n'.join(map(str, sorted(list(A.symmetric_difference(B))))))


