import numpy
N = int(input())
A = numpy.array([input().split() for _ in range(N)], float)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(A))


