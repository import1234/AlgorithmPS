c,r=map(int,input().split())
k=int(input())
if c*r<k:print(0);exit()
l=[[0]*c for _ in' '*r]
d=[(-1,0),(0,1),(1,0),(0,-1)]
curx,cury=r,0
t=0
dx,dy=d[t]
C=1
while 1:
    while 0<=curx+dx<r and 0<=cury+dy<c and l[curx+dx][cury+dy]==0:
        curx+=dx
        cury+=dy
        l[curx][cury]=C
        if C==k:print(cury+1,r-curx);exit()
        C+=1
    t=(t+1)%4
    dx,dy=d[t]