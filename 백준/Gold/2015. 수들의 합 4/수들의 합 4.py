n,k=map(int,input().split())
l=[*map(int,input().split())]

c=t=0
d={}
for x in l:
    t+=x
    d[t]=d.get(t,0)+1
t=0
for x in l:
    t+=x
    c+=d.get(k,0)
    if d.get(t):d[t]-=1
    k+=x
print(c)