import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(numpy.std(A))


