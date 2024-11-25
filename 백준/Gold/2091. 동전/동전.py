X,A,B,C,D=map(int,input().split())

dp=[[0]*4]
for x in range(1,X+1):
    k=[]
    for y in range(4):
        c=[1,5,10,25][y]
        if x-c>=0 and dp[x-c][0]+5*dp[x-c][1]+10*dp[x-c][2]+25*dp[x-c][3]==x-c and dp[x-c][y]+1<=[A,B,C,D][y]:
            t=dp[x-c][:]
            t[y]+=1
            k.append(t)
    ans=[0]*4
    M=0
    for y in k:
        if sum(y)>M:
            M=sum(y)
            ans=y
    dp.append(ans)

print(*dp[X])