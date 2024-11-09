#에라토스테네스의 체
n=int(input())
p=[]
dp=[1]*(n+1)
dp[0]=dp[1]=0
for x in range(2,n+1):
    if dp[x]:
        p.append(x)
        y=x
        while y*x<n+1:
            dp[y*x]=0
            y+=1
count=p1=p2=t=0
lp=len(p)
while 1:
    while p1<lp and t<n:
        t+=p[p1]
        p1+=1
        if t==n:count+=1
    while p2<lp and (t>=n or p1==lp):
        t-=p[p2]
        p2+=1
        if t==n:count+=1
    if p1==lp and p2==lp:break
print(count)