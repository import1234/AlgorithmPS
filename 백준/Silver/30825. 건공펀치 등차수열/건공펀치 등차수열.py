n,k=map(int,input().split())
l=[*map(int,input().split())]
a=l[0]
s=0
for x in range(1,n):
    t=a+x*k
    if t-l[x]>=0:s+=t-l[x]
    else:a+=l[x]-t;s+=(l[x]-t)*x
print(s)