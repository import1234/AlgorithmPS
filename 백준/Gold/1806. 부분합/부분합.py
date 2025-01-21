f=lambda:map(int,input().split())
n,s=f()
l=[0]+[*f()]

p1=1
p2=0

ans=float('inf')
t=0
while 1:
    if t<s:
        if p1==n+1:break
        t+=l[p1]
        p1+=1
    else:
        if p1==p2:break
        ans=min(ans,p1-p2)
        t-=l[p2]
        p2+=1

print(ans if ans!=float('inf') else 0)