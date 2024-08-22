n=int(input())
l=[0]+[*map(int,input().split())]
dp=[0]*(n+1)
for x in range(1,n+1):
    M=0
    for y in range(x):
        if l[y]<l[x] and M<dp[y]:M=dp[y]
    dp[x]=M+1

R=v=max(dp)
r=[]
for x in range(dp.index(v),-1,-1):
    if v and dp[x]==v:
        r.append(l[x])
        v-=1
r.reverse()
print(R)
print(*r)