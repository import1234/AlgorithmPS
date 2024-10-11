for x in range(int(input())):
    n=int(input())
    l=[*zip(map(int,input().split()),range(n))]
    s=sorted(l,reverse=1)
    ans=0
    p=0
    for a,b in s:
        if b<p:continue
        for y in range(p,b):
            ans+=a-l[y][0]
        p=b+1
    print(ans)