n=int(input())
m=int(input())
d={}
for x in'0'*m:
    u,v,w=map(int,input().split())
    if u not in d:d[u]={}
    if not(v in d[u] and w>d[u][v]):d[u][v]=w
k,e=map(int,input().split())
r={k:[0,[k]]} #확정
s={} #확정 안된 곳
while 1:
    if k in d:
        for x in d[k]:
            if x in r:continue
            if not(x in s and s[x][0]<r[k][0]+d[k][x]):
                s[x]=[r[k][0]+d[k][x],r[k][1]+[x]]
    if e in r:break
    
    m=float('inf')
    for x in s:
        if s[x][0]<m:
            m=s[x][0]
            k=x
    
    r[k]=[m,s[k][1][:]]
    del s[k]

print(r[e][0])
print(len(r[e][1]))
print(*r[e][1])