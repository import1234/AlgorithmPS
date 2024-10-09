from itertools import combinations as c
n,k=map(int,input().split())
l=[*map(int,input().split())]
dp=[-1]*(n+1)
p=set(l)
for y in c(l,2):p.add(sum(y))

q=[0]
count=0
for i in range(n):
    count+=1
    t=[]
    for x in q:
        for y in p:
            if x+y<=n and dp[x+y]==-1:
                dp[x+y]=count
                t.append(x+y)
    q=t
    if q==[]:break
print(dp[n])