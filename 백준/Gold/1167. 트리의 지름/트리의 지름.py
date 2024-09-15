from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
V=int(input())
d=defaultdict(dict)
for v in range(1,V+1):
    t=[*map(int,sys.stdin.readline().split())]
    for x in range(len(t)//2-1):
        d[t[0]][t[2*x+1]]=t[2*x+2]

def dfs(n,dist):
    global i,M
    visited.add(n)
    if dist>M:
        M=dist
        i=n
    for x in d[n]:
        if x not in visited:
            dfs(x,dist+d[n][x])
visited=set()
M=i=0
dfs(1,0)
visited=set()
M=0
dfs(i,0)
print(M)