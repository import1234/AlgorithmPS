from collections import defaultdict
f=lambda:map(int,input().split())
n,k=f()
l=[]
d=defaultdict(list)
for x in range(n):
    l.append([*f()])
    for y in range(n):
        if l[x][y]!=0:d[l[x][y]].append([x,y])
S,X,Y=f()
for _ in range(S):
    t=defaultdict(list)
    for i in sorted(d.keys()):
        for x,y in d[i]:
            for a,b in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=a<n and 0<=b<n and l[a][b]==0:l[a][b]=i;t[i].append([a,b])
    d=t
print(l[X-1][Y-1])