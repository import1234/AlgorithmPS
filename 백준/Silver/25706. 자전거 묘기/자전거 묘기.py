n,*l=map(int,open(0).read().split())
dp=[0]*n
for x in range(n):dp[n-x-1]=dp[n-x+l[n-x-1]]+1 if l[n-x-1]<x else 1
print(*dp)