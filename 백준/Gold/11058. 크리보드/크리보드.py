n=int(input())
dp=[*range(n+1)]
for x in range(n):
    if x-3>=0:
        dp[x]=max(dp[x],dp[x-3]*2)
        i=1
        while x+i<=n:
            dp[x+i]=max(dp[x+i],dp[x-3]*(2+i))
            i+=1
print(dp[-1])