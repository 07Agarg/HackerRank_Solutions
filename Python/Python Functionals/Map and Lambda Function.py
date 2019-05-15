cube = lambda x: x*x*x# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1]
    [fib.append(fib[i - 1] + fib[i - 2]) for i in range(2, n)]
    return fib[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))