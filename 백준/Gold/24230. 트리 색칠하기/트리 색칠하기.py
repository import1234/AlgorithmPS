from collections import defaultdict as dd
n=int(input())
C=[0]+[*map(int,input().split())]

d=dd(list)
for x in range(n-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)

t={(1,C[1])}
v={1}
count=int(C[1]!=0)
while q:=t:
    t=set()
    for x,c in q:
        if d.get(x):
            for y in d[x]:
                if y in v:continue
                count+=C[y]!=c
                t.add((y,C[y]))
                v.add(y)

print(count)