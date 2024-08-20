n=int(input())
d={}
for _ in range(int(input())):
    u,v,w=map(int,input().split())
    if u not in d:d[u]={}
    if v in d[u]:d[u][v]=min(d[u][v],w)
    else:d[u][v]=w
k,e=map(int,input().split())

r,s={k:0},{}
while 1:
    if k in d:
        for x in d[k]:
            if x in r:continue
            if x in s:s[x]=min(s[x],r[k]+d[k][x])
            else:s[x]=r[k]+d[k][x]

    m=float('inf')
    for x in s:
        if s[x]<m:m=s[x];k=x
    
    r[k]=m
    del s[k]
    if e in r:break
print(r[e])