import sys
from collections import defaultdict as dic
i=sys.stdin.readline
n,m=map(int,i().split())

l=[*map(int,i().split())]
d=dic(dict)
for x in range(1,n):
    d[x+1][l[x]]=1
    d[l[x]][x+1]=1
l=[0]*(n+1)

for x in range(m):
    a,b=map(int,i().split())
    l[a]+=b

v=set()
q={1}
while q:
    t=set()
    for x in q:
        if x not in v:
            v.add(x)
            for k in d[x]:
                if k not in v:
                    t.add(k)
                    l[k]+=l[x]
    q=t


print(*l[1:])