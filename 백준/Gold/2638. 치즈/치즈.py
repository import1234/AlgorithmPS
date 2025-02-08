f=lambda:map(int,input().split())
m,n=f()
l=[[*f()]for x in' '*m]
c=0
while 1:
    D=[[4*[0]for _ in' '*n]for _ in' '*m]

    v={(0,0)};t={(0,0)}
    while q:=t:
        t=set()
        for x,y in q:
            for a,b,z in[(1,0,0),(-2,0,1),(1,1,2),(0,-2,3)]:
                x+=a;y+=b
                if 0<=x<m and 0<=y<n:
                    if l[x][y]==1:D[x][y][z]=1
                    if l[x][y]==0 and(x,y)not in v:t.add((x,y));v.add((x,y))

    e=1
    for x in range(m):
        for y in range(n):
            if sum(D[x][y])>=2:l[x][y]=0;e=0
    if e:break
    c+=1
print(c)