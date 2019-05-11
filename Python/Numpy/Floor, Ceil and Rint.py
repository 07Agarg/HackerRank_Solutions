import numpy
numpy.set_printoptions(sign = ' ')
a = numpy.array(input().split(), float)
print(numpy.floor(a), numpy.ceil(a), numpy.rint(a), sep = "\n")


