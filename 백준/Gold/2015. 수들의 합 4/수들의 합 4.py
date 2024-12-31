n,k=map(int,input().split())
l=[*map(int,input().split())]
c=t=u=0
d={}
for x in l:d[u]=d.get(u:=u+x,0)+1
for x in l:
    c+=d.get(k,0)
    if d.get(t:=t+x):d[t]-=1
    k+=x
print(c)