n=int(input())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
C=[*map(int,input().split())]
dp=[-1]*(n+1)
for x in range(n):
    a,b,c=sorted([A[x],B[x],C[x]])
    dp[x+1]=max(dp[x]+1,a)
    if dp[x+1]>c or dp[x+1]==-1:print('NO');exit()
print('YES')