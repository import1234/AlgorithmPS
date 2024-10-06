n=int(input())
l=[[*map(int,input().split())]for x in' '*n]
dp=[[3*[0]for x in' '*n]for x in' '*n]#h,d,v
dp[0][1][0]=1
for x in range(n):
    for y in range(2,n):
        if l[x][y]==1:continue
        dp[x][y][0]+=sum(dp[x][y-1][:2])
        if x!=0:dp[x][y][2]+=sum(dp[x-1][y][1:])
        if x!=0 and y!=0 and l[x-1][y]!=1 and l[x][y-1]!=1:dp[x][y][1]=sum(dp[x-1][y-1])
print(sum(dp[-1][-1]))