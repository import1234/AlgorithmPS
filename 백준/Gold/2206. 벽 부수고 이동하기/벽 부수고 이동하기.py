m,n=map(int,input().split())
l=[[*input()]for _ in range(m)]
for x in range(m):
    for y in range(n):l[x][y]=int(l[x][y])
N=[[0]*n for _ in range(m)] #before break
Y=[[0]*n for _ in range(m)] #after break

t={(0,0,0)} #x좌표, y좌표, 벽 뚫었는지 toggle
count=0
while q:=t:
    t=set()
    count+=1
    for x,y,br in q:
        if x==m-1 and y==n-1:print(count);exit()
        if br:
            if Y[x][y]!=0:continue
            else:Y[x][y]=count
        else:
            if N[x][y]!=0:continue
            else:N[x][y]=count
        for a,b in[(0,1),(0,-2),(1,1),(-2,0)]:
            x+=a;y+=b
            if 0<=x<m and 0<=y<n:
                if l[x][y]==0:t.add((x,y,br))
                elif l[x][y]==1 and br==0:t.add((x,y,1))
print(-1)