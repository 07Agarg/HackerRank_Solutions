if __name__ == '__main__':
    marksheet = [[input(), float(input())]  for _ in range(int(input()))]
    second_highest = sorted(set([marks for name, marks in marksheet]))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


    """
    for _ in range(int(input())):
        name = input()
        score = float(input())
    """
