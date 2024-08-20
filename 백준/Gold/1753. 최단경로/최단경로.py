import sys
i=sys.stdin.readline

#정점 리스트
d={}
V,E=map(int,i().split())
k=int(i())
for x in'0'*E:
    u,v,w=map(int,i().split())
    if u not in d:d[u]={}
    if v in d[u]:d[u][v]=min(d[u][v],w)
    else:d[u][v]=w

#데이크스트라
r={k:0} #최단거리가 확정된 점
s={} #최단거리가 확정 안된 점(inf는 생략)
#k 최단거리가 가장 최근에 확정된 점
while 1:
    if k in d:
        for x in d[k]:
            if x in r:continue #이미 최단거리가 확정된 점이면
            if x in s:s[x]=min(s[x],r[k]+d[k][x])
            else:s[x]=r[k]+d[k][x]
    if s=={}:break
    m=float('inf')
    for x in s:
        if s[x]<m:
            m=s[x]
            k=x
    r[k]=m
    del s[k]

#출력
for x in range(1,V+1):
    if x in r:print(r[x])
    else:print('INF')