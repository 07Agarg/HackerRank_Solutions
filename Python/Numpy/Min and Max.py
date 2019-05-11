import numpy
N, M = map(int, input().split())
print(numpy.max(numpy.min(numpy.array([input().split() for _ in range(N)], int), axis = 1)))


