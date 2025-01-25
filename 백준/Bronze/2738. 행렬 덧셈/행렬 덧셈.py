f=lambda:map(int,input().split())
n,m=f()
l=[]
for x in range(n):l.append([*f()])
for x in range(n):
    t=[*f()]
    for y in range(m):l[x][y]+=t[y]
for x in l:
    print(*x)