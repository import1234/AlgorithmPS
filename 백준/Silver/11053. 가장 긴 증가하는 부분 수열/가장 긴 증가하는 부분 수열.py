n=int(input())
l=[0]+[*map(int,input().split())]
dp=[0]+[0]*n
for x in range(1,n+1):
    m=0
    for y in range(x):
        if m<=dp[y] and l[y]<l[x]:m=dp[y]
    dp[x]=m+1
print(max(dp))