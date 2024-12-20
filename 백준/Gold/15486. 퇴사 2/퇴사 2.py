import sys
i=sys.stdin.readline
n=int(i())
d={}
for x in range(n):
    a,b=map(int,i().split())
    if a+x in d:
        d[a+x].append([a,b])
    else:
        d[a+x]=[[a,b]]

l=[0]*(n+1)
for x in range(n+1):
    t=0
    if x in d:
        for a,b in d[x]:
            t=max(t,l[x-a]+b)
    l[x]=max(l[x-1],t)
print(l[-1])