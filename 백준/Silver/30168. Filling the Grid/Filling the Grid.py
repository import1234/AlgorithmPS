mod=10**9+7
f=lambda:map(int,input().split())
h,w=f()
r=[*f()]
c=[*f()]
l=[[1]*w for x in range(h)]

ans=1
for x in range(h):
    for y in range(w):
        s=set()
        if y<r[x]:s.add(1)
        elif y==r[x]:s.add(0)
        if x<c[y]:s.add(1)
        elif x==c[y]:s.add(0)
        if s==set():ans*=2;ans%=mod
        elif len(s)==1:pass
        else:print(0);exit()
print(ans)