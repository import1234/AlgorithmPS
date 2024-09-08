from collections import defaultdict
from sys import stdin
n,m=int(input()),int(input())
d=defaultdict(dict)
for x in range(m):
    a,b,c=map(int,stdin.readline().split())
    a-=1;b-=1
    if b in d[a]:d[a][b]=min(d[a][b],c)
    else:d[a][b]=c

#거리 초기화
l=[]
for x in range(n):
    l.append([])
    for y in range(n):
        if x==y:l[x].append(0)
        else:l[x].append(d[x][y] if y in d[x] else float('inf'))

for x in range(n):
    for y in range(n):
        for z in range(n):
            l[y][z]=min(l[y][z],l[y][x]+l[x][z])

for x in l:
    s=''
    for y in x:
        if y==float('inf'):s+='0 '
        else:s+=str(y)+' '
    print(s)