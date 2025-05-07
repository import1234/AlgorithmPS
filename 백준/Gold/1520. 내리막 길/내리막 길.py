import sys
sys.setrecursionlimit(25000)
n,m=map(int,input().split())
l=[[*map(int,input().split())]for x in' '*n]

dp=[[-1]*m for x in' '*n]
dp[n-1][m-1]=1

v=set()
def f(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    v.add((x,y))
    s=0
    for a,b in [(-1,0),(0,1),(1,0),(0,-1)]:
        if 0<=x+a<n and 0<=y+b<m and (x+a,y+b)not in v and l[x+a][y+b]<l[x][y]:s+=f(x+a,y+b)
    dp[x][y]=s
    v.remove((x,y))
    return s
    
f(0,0)
print(dp[0][0])