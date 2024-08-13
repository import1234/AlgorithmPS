n=int(input())
l=[[*map(int,input().split())]for _ in range(n)]
r=[0]*n
r[0]=l[0][0]
for x in range(1,n):
    t=[0]*n
    for y in range(x):
        t[y]=max(r[y]+l[x][y],t[y])
        t[y+1]=max(r[y]+l[x][y+1],t[y+1])
    r=t

print(max(r))