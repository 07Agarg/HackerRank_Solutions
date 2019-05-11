if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    #i=0
    for i in range(0, n):
        if zes == max(arr):
            arr.remove(max(arr))
        #i+=1
    print(max(arr))
