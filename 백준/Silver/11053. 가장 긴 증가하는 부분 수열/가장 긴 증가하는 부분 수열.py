n=int(input())
l=[0]+[*map(int,input().split())]
dp=[0]*(n+1)
for x in range(1,n+1):
    M=0
    for y in range(x):
        if l[y]<l[x] and dp[y]>M:M=dp[y]
    dp[x]=M+1
print(max(dp))