n,lim=map(int,input().split())
V,W=[0],[0]
for x in range(n):a,b=map(int,input().split());W+=[a];V+=[b]
dp=[[0 for x in'0'*(lim+1)]for y in'0'*(n+1)]
for idx in range(1,n+1):
    for w in range(1,lim+1):
        if W[idx]>w:dp[idx][w]=dp[idx-1][w]
        else:dp[idx][w]=max(V[idx]+dp[idx-1][w-W[idx]],dp[idx-1][w])
print(dp[-1][-1])