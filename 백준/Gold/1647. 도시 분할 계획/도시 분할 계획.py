import heapq
from collections import defaultdict as dd
f=lambda:map(int,input().split())
n,m=f()
d=dd(dict)
inf=float('inf')
for x in' '*m:
    a,b,c=f()
    d[a][b]=min(d[a].get(b,inf),c)
    d[b][a]=min(d[b].get(a,inf),c)

s={1} #시작 노드: 1
heap=[(d[1][x],x) for x in d[1].keys()]
heapq.heapify(heap)
mst=[]
while len(s)<n:
    c,b=heapq.heappop(heap)
    
    if b in s:continue
    mst.append((c,b))
    s.add(b)
    
    for x in d[b].keys():
        if x in s:continue #중복 노드 제거
        heapq.heappush(heap,(d[b][x],x)) #가중치, 끝노드

mst.sort()
mst.pop()
print(sum(x[0]for x in mst))