from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

def dfs(p, now):
    global c
    for x in d[now]:
        if x!=p:
            if C[now]!=C[x]:c+=1
            dfs(now,x)

n=int(input())
C=[0]+list(map(int,input().split()))
d=defaultdict(list)

for x in' '*(n-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)

c=int(C[1]!=0)
dfs(0,1)
print(c)