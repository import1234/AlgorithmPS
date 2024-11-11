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
    if t==n:
        count+=1
        if p2>=lp:break
        t+=p[p2]
        p2+=1
    elif t<n:
        if p2>=lp:break
        t+=p[p2]
        p2+=1
    else:
        t-=p[p1]
        p1+=1
print(count)