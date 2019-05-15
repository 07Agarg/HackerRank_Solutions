# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N, Student = int(input()), namedtuple('Student', input().split())
print("{:.2f}".format(sum(int(Student(*input().split()).MARKS) for _ in range(N)) / N))
