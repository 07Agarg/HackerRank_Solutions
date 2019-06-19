# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as f:
        print("Error Code:", f)
