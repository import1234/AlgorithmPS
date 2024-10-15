n,k=map(int,input().split())
coin=[int(input()) for x in range(n)]
dp=[1]+[0]*k
for c in sorted(coin):
    for x in range(c,k+1):
        dp[x]+=dp[x-c]
print(dp[-1])