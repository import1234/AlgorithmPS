d,m=map(int,input().split())
l={0:1}
for x in [*range(1,d//2+1)]+[*range(d//2-1,0,-1)]:
    t={}
    for y in l:
        if y-1>0:t[y-1]=(t.get(y-1,0)+l[y])%m
        if y+1<=x:t[y+1]=(t.get(y+1,0)+l[y])%m
    l=t
print(l[1])