n=int(input())
l=list(map(int,input().split()))
d=dict()
for x in l:
    for y in list(d.keys()):
        if y<x:
            if d.get(x):d[x]=max(d[y]+1, d[x])
            else:d[x]=d[y]+1
    if not d.get(x):d[x]=1
M=0
for x in list(d.keys()):
    if d[x]>M:M=d[x]
print(M)