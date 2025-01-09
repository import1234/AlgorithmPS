f=lambda:map(int,input().split())
n,m=f()
l=[0]*(n+1)
d={}
for _ in ' '*m:
    a,b=f()
    d.setdefault(a,[]).append(b)
    d.setdefault(b,[]).append(a)

for x in range(1,n+1):
    if l[x]:continue
    q=[x];l[x]=1
    while q:
        x=q.pop()
        for y in d.get(x,[]):
            if l[y]==l[x]:print(0);exit()
            if not l[y]:l[y]=-l[x];q.append(y)
print(1)