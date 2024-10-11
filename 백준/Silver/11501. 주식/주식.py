for x in range(int(input())):
    input()
    l=[*map(int,input().split())]
    c=ans=0
    for x in l[::-1]:
        if x>c:c=x
        else:ans+=c-x
    print(ans)