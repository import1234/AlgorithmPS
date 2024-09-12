INF=float('inf')
n,m=int(input()),int(input())

#거리 초기화
l=[[INF]*n for _ in range(n)]
for x in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    l[a][b]=min(l[a][b],c)

for x in range(n):
    l[x][x]=0
    for y in range(n):
        for z in range(n):
            l[y][z]=min(l[y][z],l[y][x]+l[x][z])

for x in l:
    for y in x:
        print(0 if y==INF else y)