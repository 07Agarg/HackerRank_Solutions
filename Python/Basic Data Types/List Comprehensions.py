if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[p, q, r] for p in range(0, x + 1) for q in range(0, y + 1) for r in range(0, z + 1) if (p + q + r != n)]
    print(coordinates)
