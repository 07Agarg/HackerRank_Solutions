from fractions import Fraction
from functools import reduce

def product(fracs):
    # complete this line with a reduce statement
    t = reduce(lambda f1,f2: f1 * f2, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)