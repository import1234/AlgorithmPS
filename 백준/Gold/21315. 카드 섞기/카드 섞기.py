from math import log2

def f(t,k):
    r=[]
    for x in range(k+1):
        for y in range(max(1,2**(x-1))):r.append(t[-2**x+y])
    return r

def g(t,k):
    return f(t[-2**k:],k)+t[:-2**k]

n=int(input())
l=[i+1 for i in range(n)]
a=[*map(int,input().split())]

n=int(log2(n))+1
for x in range(1,n):
    t=g(l,x)
    for y in range(1,n):
        r=g(t,y)
        if r==a:print(x,y);exit()