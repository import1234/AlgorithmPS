from itertools import combinations as c
import sys
sys.setrecursionlimit(10**6)
d={}
n=int(input())
M=0
for x in range(n-1):
    u,v,w=map(int,input().split())
    if u not in d:d[u]={v:[w,0]}
    else:d[u][v]=[w,0]

def f(a):
    l=[]
    if a in d:
        for x in d[a]:
            t=f(x)
            d[a][x][1]=t
            l.append(d[a][x][0]+t)
    return max(l if l else[0])

def g(a):
    global M
    if a in d:
        s=[]
        for x in d[a]:s.append(sum(d[a][x]));g(x)
        if M<max(s):M=max(s)
        for x,y in c(s,2):
            if M<x+y:M=x+y

f(1);g(1)
print(M)
