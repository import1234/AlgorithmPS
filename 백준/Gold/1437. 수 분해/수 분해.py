n=int(input())
if n<=4:print(n);exit()
dp=[0,1,2,3,4]+[0]*(n-3)
for x in range(5,n+1):
    dp[x]=dp[x-3]*3%10007
print(dp[n])