f=lambda:[*map(int,input().split())]
n,m=f()
l=f()
k=f()

t1=[]
t2=[]
t=c=0
for x in k:
    for y in' '*x:
        [t1,t2][t].append(c)
        c+=1
    t=1-t

def g(a):
    c=0
    t=0
    for x in range(n):
        if l[x]==1:
            c+=abs(x-a[t])
            t+=1
    return c

ans=10**10
if len(t1)==sum(l):
    ans=min(ans,g(t1))
if len(t2)==sum(l):
    ans=min(ans,g(t2))
print(ans)