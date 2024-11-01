n=int(input())
l=[*map(int,input().split())]
dp=[0]*n
for x in range(n):dp[n-x-1]=dp[n-x+l[n-x-1]]+1 if n-x+l[n-x-1]<n else 1
print(*dp)