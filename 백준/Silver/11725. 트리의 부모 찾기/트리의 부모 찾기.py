import sys
from collections import defaultdict as d
sys.setrecursionlimit(10**6)
n=int(input())
t=d(list)
for x in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    t[a]+=[b];t[b]+=[a]
l=[1]*(n+1);v=l[:]

def f(i):
    v[i]=0
    for x in t[i]:
        if v[x]:l[x]=i;f(x)

f(1)
print(*l[2:])