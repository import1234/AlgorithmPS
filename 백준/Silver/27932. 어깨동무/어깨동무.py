f=lambda:map(int,input().split())
n,k=f()
l=[*f()]
if n==1:print(0);exit()

def g(h):
    t=0
    for x in range(n):
        if x==0:t+=(abs(l[x+1]-l[x])>h)
        elif x==n-1:t+=(abs(l[x-1]-l[x])>h)
        else:t+=(abs(l[x+1]-l[x])>h or abs(l[x-1]-l[x])>h)
    return t

s=0;e=10**9
while s<=e:
    m=(s+e)//2
    if g(m)<=k:e=m-1
    else:s=m+1
print(s)