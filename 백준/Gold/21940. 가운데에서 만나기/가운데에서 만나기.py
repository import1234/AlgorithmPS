from collections import defaultdict as dic
n,m=map(int,input().split())
d=dic(dict)
for _ in' '*m:
    a,b,c=map(int,input().split())
    d[a-1][b-1]=min(d[a-1].get(b-1,float('inf')),c)
k=int(input())
kl=[*map(int,input().split())]

#초기화
l=[[0]*n for x in range(n)]
for x in range(n):
    for y in range(n):
        if y in d[x]:l[x][y]=d[x][y]
        elif x==y:l[x][y]=0
        else:l[x][y]=float('inf')

#플로이드 워셜
for x in range(n):
    for y in range(n):
        for z in range(n):
            l[y][z]=min(l[y][z],l[y][x]+l[x][z])

r=[]
for x in range(n):
    M=0
    for y in kl:
        if M<l[y-1][x]+l[x][y-1]:M=l[y-1][x]+l[x][y-1]
    r.append(M)
t=min(r)
for x in range(n):
    if r[x]==t:print(x+1,end=' ')