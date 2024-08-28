n,m=map(int,input().split())
a=input()
for x in range(n-1):
    p=0
    b=input()
    for y in range(1,m+1):
        if a[m-y:]==b[:y]:
            p=1
            break
    for y in range(m-1,0,-1):
        if a[:y]==b[m-y:]:
            p=1
            break
    if p==0:print(0);exit()
    a=b
print(1)