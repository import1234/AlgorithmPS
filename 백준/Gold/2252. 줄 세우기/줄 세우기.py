from collections import defaultdict as dd
f=lambda:map(int,input().split())
n,m=f()
ind=dd(int)
d=dd(list)
for x in' '*m:
    a,b=f()
    d[a].append(b)
    ind[b]+=1

t=set(range(1,n+1))-set(ind.keys())

ans=[]
while q:=t:
    t=set()
    for x in q:
        ans.append(x)
        for y in d[x]:
            ind[y]-=1
            if ind[y]==0:t.add(y)

print(*ans)