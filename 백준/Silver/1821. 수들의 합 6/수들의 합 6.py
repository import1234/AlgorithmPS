from math import comb
n,k=map(int,input().split())
c=[comb(n-1,x)for x in range(n)]
ans=[9**9]
l=[]
v=set()
def f(t):
    if t==0:
        a=0
        for x in range(n):
            a+=c[x]*l[x]
        if a==k:
            global ans
            if l<ans:ans=l[:]
    for x in range(1,n+1):
        if x not in v:
            l.append(x)
            v.add(x)
            f(t-1)
            l.pop()
            v.remove(x)
f(n)
print(*ans)