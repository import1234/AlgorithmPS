from collections import defaultdict as dd
f=lambda:map(int,input().split())
n,m=f()
l=[0]*(n+1)
d=dd(list)
for x in' '*m:
    a,b=f()
    d[a].append(b)
    d[b].append(a)

for x in range(1,n+1):
    if l[x]!=0:continue
    l[x]=1
    t={x}
    while q:=t:
        t=set()
        for x in q:
            for y in d[x]:
                if l[x]==-l[y]:continue
                if l[y]!=0:print(0);exit()
                l[y]=-l[x]
                t.add(y)
print(1)