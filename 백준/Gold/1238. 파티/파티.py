from collections import defaultdict as d
N,M,X=map(int,input().split())
d1=d(dict)
d2=d(dict)
for x in range(M):
    a,b,c=map(int,input().split())
    d1[a][b]=c
    d2[b][a]=c

#Dijkstra 1
k=X #시작점
V1={k:0} #거리가 결정된 집합
S={} #거리가 결정되지 않은 집합
while 1:
    for x in d1[k]:
        if x in V1:continue
        if x in S:S[x]=min(S[x],V1[k]+d1[k][x])
        else:S[x]=V1[k]+d1[k][x]
    if S=={}:break
    
    M=float('inf')
    for x in S:
        if S[x]<M:M=S[x];k=x
    V1[k]=M
    del S[k]

#Dijkstra 2
k=X #시작점
V2={k:0} #거리가 결정된 집합
S={} #거리가 결정되지 않은 집합
while 1:
    for x in d2[k]:
        if x in V2:continue
        if x in S:S[x]=min(S[x],V2[k]+d2[k][x])
        else:S[x]=V2[k]+d2[k][x]
    if S=={}:break
    
    M=float('inf')
    for x in S:
        if S[x]<M:M=S[x];k=x
    V2[k]=M
    del S[k]

M=0
for x in range(1,N+1):
    if M<V1[x]+V2[x]:M=V1[x]+V2[x]
print(M)