import sys
from collections import defaultdict

input = sys.stdin.readline

n,m,r=map(int,input().split())
d=defaultdict(set)
for x in range(m):
    a,b=map(int,input().split())
    d[a].add(b)
    d[b].add(a)

visited=set()
count=1
t={r}
ans=0
depth=0

while q:=t:
    t=set()
    for x in q:
        if x not in visited:
            t.update(d[x])
            visited.add(x)
            ans+=count*depth
            count+=1
    depth+=1

print(ans)