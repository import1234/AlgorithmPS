from collections import defaultdict
n,p=map(int,input().split())
l=[*map(int,input().split())]
d=defaultdict(list)
r=0
for x in range(n):d[l[x]].append(x+1)
t=[d[0]]
while q:=t:
    t=[]
    for x in q:
        if len(x)>p:r+=(len(x)-2)//(p-1)
        for y in x:
            if d.get(y):t.append(d[y])
print(r)