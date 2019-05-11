import numpy
N, M, P = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(M)], int)
print(numpy.concatenate([A, B]))

