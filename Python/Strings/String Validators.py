if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))

"""
    l1 = []
    for i in range(len(s)):
        l.append(s[i].isalpha())
        l1.append(s[i].isdigit())
    #print(any(l), any(l1), sep="\n")
    #print(s.isalnum(), s.isalpha(), !s.isdigit(), !s.islower(), !s.isupper(), sep ="\n")
"""
