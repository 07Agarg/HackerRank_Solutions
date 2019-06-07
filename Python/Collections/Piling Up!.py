# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    N, A = int(input()), list(map(int, input().split()))
    #i, j, k = 0, N - 1, k = 1
    i = 0
    while(i < N-1 and A[i] >= A[i+1]):
        i += 1
    while(i < N-1 and A[i] <= A[i+1]):
        i += 1
    if(i == N - 1):
        print("Yes")
    else:
        print("No")
