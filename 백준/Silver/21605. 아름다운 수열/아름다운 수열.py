dp=[[0],[-1,1],[1,-1,-1,1],[1,1,-1,-1,-1,1],[1,1,-1,-1,1,-1,-1,1],[1,1,-1,-1,1,-1,1,-1,-1,1]]

n=int(input())
for x in range(6,n+1):
    dp.append([1,1]+dp[x-3]+[-1,-1,-1,1])
print(*dp[n])