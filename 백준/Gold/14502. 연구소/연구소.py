import copy
f=lambda:map(int,input().split())
n,m=f()
l=[[*f()] for x in' '*n]
v=set()
for x in range(n):
    for y in range(m):
        if l[x][y]==2:v.add((x,y))

ans=[]

def g():
    # print()
    # for x in l:print(*x)

    L=copy.deepcopy(l)
    t=v.copy()
    while q:=t:
        t=set()
        for x,y in q:
            for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
                x+=a;y+=b
                if 0<=x<n and 0<=y<m and L[x][y]==0:
                    L[x][y]=2
                    t.add((x,y))
    c=0
    for x in range(n):
        for y in range(m):
            if L[x][y]==0:c+=1
    ans.append(c)
    # print()
    # for x in L:print(*x)
    # print(ans)

def f(t):
    if t==3:g();return
    for x in range(n):
        for y in range(m):
            if l[x][y]==0:
                l[x][y]=1
                f(t+1)
                l[x][y]=0

f(0)
print(max(ans))