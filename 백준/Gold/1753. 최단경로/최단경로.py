import sys,heapq
from collections import defaultdict
i=sys.stdin.readline

d=defaultdict(dict)
n,e=map(int,i().split())
k=int(i()) #시작점
for x in'0'*e:
    u,v,w=map(int,i().split())
    d[u][v]=min(d[u].get(v,float('inf')),w)

V={k:0} #최단거리가 확정된 노드
S={} #최단거리가 확정 안된 노드(inf는 생략)
q=[] #최소 힙
#k 최단거리가 가장 최근에 확정된 노드
while 1:
    for x in d[k]:
        if x in V:continue #이미 최단거리가 확정된 노드면
        S[x]=min(S.get(x,float('inf')),V[k]+d[k][x])
        heapq.heappush(q,(S[x],x))
    if S=={}:break #최단거리가 확정되지 않은 노드가 없으면 종료

    m=float('inf')
    while 1:
        m,k=heapq.heappop(q)
        if k not in V:break
    
    V[k]=m #해당 노드 V로 확정
    del S[k] #S에서는 제거

#출력
for x in range(1,n+1):print(V[x] if x in V else 'INF')