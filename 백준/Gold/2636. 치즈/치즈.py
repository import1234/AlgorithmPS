m,n=map(int,input().split())
l=[input().split()for x in' '*m]

count=0
prev=sum(x.count('1') for x in l)
while 1:
    d=set()
    v=set()
    t={(0,0)}
    while q:=t: #bfs
        t=set()
        for x,y in q:
            v.add((x,y))
            for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
                x+=a;y+=b
                if 0<=x<m and 0<=y<n and (x,y) not in v:
                    if l[x][y]=='1':d.add((x,y))
                    else:t.add((x,y))
    for x,y in d:l[x][y]='0'
    if d==set():break
    prev=len(d)
    count+=1
print(count,prev)