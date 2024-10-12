for x in range(int(input())):
    n=int(input())
    coin=[*map(int,input().split())]
    k=int(input())
    dp=[[0]*n for x in range(k+1)]
    for x in range(k+1):
        for y in range(n):
            if x==0:dp[x][y]=1;continue
            for z in range(n):
                if coin[z]>coin[y]:break
                dp[x][y]+=dp[x-coin[z]][z] if k-coin[z]>=0 else 0
    print(dp[-1][-1])