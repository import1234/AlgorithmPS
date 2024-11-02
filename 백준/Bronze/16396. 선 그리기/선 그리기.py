dp=[0]*10001
for x in range(int(input())):
    a,b=map(int,input().split())
    for y in range(a,b):dp[y]=1
print(sum(dp))