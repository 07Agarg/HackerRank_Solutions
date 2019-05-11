import numpy
A, B = [numpy.array([input().split()], int) for _ in range(2)]
print(numpy.inner(A, B)[0][0])
print(numpy.outer(A, B))


