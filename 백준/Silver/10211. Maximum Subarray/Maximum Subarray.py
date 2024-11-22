for x in' '*int(input()):
    input()
    M=-10**4
    a=0
    for x in map(int,input().split()):
        if a<0:a=x
        else:a+=x
        M=max(a,M)
    print(M)