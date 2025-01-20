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
heap=[(d[1][x],1,x) for x in d[1].keys()]
heapq.heapify(heap)
mst=[]
while len(s)<n:
    c,a,b=heapq.heappop(heap)
    
    if a in s and b in s:continue
    mst.append((c,a,b))
    t=b if a in s else a
    s.add(t)
    
    for x in d[t].keys():
        if x in s:continue #중복 노드 제거
        heapq.heappush(heap,(d[t][x],t,x)) #가중치, 시작노드, 끝노드

mst.sort()
mst.pop()
print(sum(x[0] for x in mst))