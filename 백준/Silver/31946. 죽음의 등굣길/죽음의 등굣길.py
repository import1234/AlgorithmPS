from collections import deque
n=int(input())
m=int(input())
l=[[*map(int,input().split())]for x in' '*n]
c=l[0][0]
v={(0,0)}
X=int(input())

q=deque([(0,0)])
while len(q)>0:
    a,b=q.popleft()
    if a==n-1 and b==m-1:print('ALIVE');exit()
    for x in range(a-X,a+X+1):
        for y in range(b-X,b+X+1):
            if abs(a-x)+abs(b-y)<=X and 0<=x<n and 0<=y<m and l[x][y]==c and (x,y)not in v:
                q.append((x,y))
                v.add((x,y))
print('DEAD')