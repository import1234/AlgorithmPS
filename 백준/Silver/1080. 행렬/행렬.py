m,n=map(int,input().split())
l=[[*map(int,[*input()])]for x in range(m)]
k=[[*map(int,[*input()])]for x in range(m)]


c=0
for x in range(m):
    for y in range(n):
        if l[x][y]!=k[x][y]:
            if x+2<m and y+2<n:
                c+=1
                for t1 in range(3):
                    for t2 in range(3):
                        l[x+t1][y+t2]=1-l[x+t1][y+t2]

if all(l[x][y]==k[x][y] for x in range(m) for y in range(n)):print(c)
else:print(-1)