n=int(input())
dp=[*range(n+1)]
for x in range(3,n):
    for y in range(n-x+1):
        dp[x+y]=max(dp[x+y],dp[x-3]*(2+y))
print(dp[-1])