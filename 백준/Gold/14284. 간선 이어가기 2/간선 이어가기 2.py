import sys
from collections import defaultdict
i=sys.stdin.readline

d=defaultdict(dict)
n,m=map(int,i().split())
for x in range(m):
    u,v,w=map(int,i().split())
    d[u][v]=min(d[u].get(v,float('inf')),w)
    d[v][u]=min(d[v].get(u,float('inf')),w)
k,e=map(int,input().split())

V={k:0}
s={}
while 1:
    for x in d[k]:
        if x in V:continue
        s[x]=min(s.get(x,float('inf')),V[k]+d[k][x])
    if s=={}:break

    m=float('inf')
    for x in s:
        if s[x]<m:m=s[x];k=x
    V[k]=m
    del s[k]

print(V[e])