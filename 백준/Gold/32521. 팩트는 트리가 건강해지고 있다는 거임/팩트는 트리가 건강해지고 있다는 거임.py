import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict as dd
f=lambda:map(int,input().split())
N,K=f()
H=[0]+[*f()]
d=dd(list)
for x in range(N-1):
    a,b=f()
    d[a].append(b)
    d[b].append(a)

v=set()
count=0
def dfs(x):
    global count
    v.add(x)
    k=H[x]
    t=[]
    for y in d[x]:
        if y in v:continue
        t.append(dfs(y))
    t.sort()
    for x in t:
        if k+x>K:count+=1
        else:k+=x
    return k
dfs(1)
print(count)