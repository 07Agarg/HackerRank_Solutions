# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
ls = []
for i in range(X):
    ls.append(list(map(float, input().split())))

for i in zip(*ls):
    print(sum(i)/len(i))
