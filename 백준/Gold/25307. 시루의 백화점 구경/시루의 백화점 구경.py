from collections import deque
f=lambda:map(int,input().split())
m,n,k=f()
man=deque()
q=deque()
l=[]
yes=0
for x in range(m):
    l.append([])
    t=[*f()]
    for y in range(n):
        l[-1].append(t[y])
        if t[y]==2:yes=1
        if t[y]==3:man.append((x,y))
        elif t[y]==4:q.append((x,y))
if yes==0:print(-1);exit()

v=set(man)
while man:
    for _ in range(len(man)):
        x,y=man.popleft()
        l[x][y]=3
        if k>0:
            for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
                x+=a;y+=b
                if 0<=x<m and 0<=y<n and (x,y)not in v:
                    man.append((x,y))
                    v.add((x,y))
    k-=1

c=0
v=set(q)
while q:
    for _ in range(len(q)):
        x,y=q.popleft()
        for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
            x+=a;y+=b
            if 0<=x<m and 0<=y<n and l[x][y]in[0,2] and (x,y)not in v:
                if l[x][y]==2:print(c+1);exit()
                q.append((x,y))
                v.add((x,y))
    c+=1

print(-1)