f=lambda:map(int,input().split())
n,m=f()
l=[*f()]
d={}
for x in range(m):d[x+1]=[l[x],set()]

a=[set()for x in' '*n]
for _ in range(2):
    for x in range(n):
        for y in f():
            if y==-1:break
            d[y][1].add(x)
    for x in d:
        if len(d[x][1])<=d[x][0]:
            for y in d[x][1]:a[y].add(x)

for x in a:print(*sorted(x)if x!=set()else['망했어요'])