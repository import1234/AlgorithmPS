from collections import deque
n=int(input())
l=[]
p=None
for x in range(n):
    l.append([*map(int,input().split())])
    if 9 in l[-1]:
        y=l[-1].index(9)
        p=(x,y)
        l[x][y]=0

ans=0
lv=2
eat=0

while 1:
    q=deque([p])
    v=set([p])
    stop=0
    c=0
    while q and stop==0:
        c+=1
        for _ in range(len(q)):
            x,y=q.popleft()
            for a,b in[(0,1),(0,-2),(1,1),(-2,0)]:
                x+=a;y+=b
                if 0<=x<n and 0<=y<n and (x,y) not in v and l[x][y]<=lv:
                    q.append((x,y))
                    v.add((x,y))
                    if 0<l[x][y]<lv:stop=1
    if len(q)==0:print(ans);exit()
    for x,y in sorted(q):
        if 0<l[x][y]<lv:
            eat+=1
            ans+=c
            l[x][y]=0
            p=(x,y)
            break

    if eat==lv:eat=0;lv+=1