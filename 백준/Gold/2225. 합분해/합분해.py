n,k=map(int,input().split())
dp=[[0]*(k+1) for _ in' '*(n+1)]
dp[0][0]=1
for y in range(1,k+1):
    for x in range(n+1):
        for z in range(x+1):
            dp[x][y]+=dp[z][y-1]
        dp[x][y]%=10**9
print(dp[n][k])