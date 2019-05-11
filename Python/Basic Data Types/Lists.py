if __name__ == '__main__':
    N = int(input())
    s = []
    for _ in range(N):
        inputs = input().split()
        if len(inputs) == 3:
            s.insert(int(inputs[1]), int(inputs[2]))
            #s[int(inputs[2])] = int(inputs[1])
        elif len(inputs) == 2:
            if inputs[0] == "remove":
                s.remove(int(inputs[1]))
            else:
                s.append(int(inputs[1]))
        else:
            if inputs[0] == "print":
                print(s)
            elif inputs[0] == "sort":
                s.sort()
            elif inputs[0] == "pop":
                s.pop()
            else :
                s.reverse()
        

