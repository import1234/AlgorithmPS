import sys
i=sys.stdin.readline
n,k=map(int,i().split())
l=[]
s=set()
for x in range(n):
    a,b=map(int,i().split())
    t=(a**2+b**2)**.5
    l.append(t)
    s.add(max(0,t-k/2))
    s.add(t+k/2)

def search_l(t):
    s=0
    e=n-1
    while s<=e:
        m=(s+e)//2
        if l[m]>=t:e=m-1
        else:s=m+1
    return s

def search_r(t):
    s=0
    e=n-1
    while s<=e:
        m=(s+e)//2
        if l[m]<=t:s=m+1
        else:e=m-1
    return e

d={}
l.sort()
for x in s:
    a=max(0,x-k/2)
    a=search_l(a)
    b=x+k/2
    b=search_r(b)
    d[x]=b-a+1

print(100/n*max(d.values()))
