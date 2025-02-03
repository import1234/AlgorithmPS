for _ in range(int(input())):
    _,n=map(int,input().split())
    l=sorted(map(int,input().split()))
    s=0;e=10**10
    while s<=e:
        m=(s+e)//2
        c=1
        t=l[0]
        for x in l[1:]:
            if x-t>=m:
                t=x
                c+=1
        if c>=n:s=m+1
        else:e=m-1
    print(e)