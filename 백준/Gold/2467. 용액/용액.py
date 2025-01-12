n=int(input())
l=[*map(int,input().split())]

ans=[float('inf'),0,0]
for x in range(n):
    s=0
    e=n-1
    t=-l[x]
    while s<=e:
        m=(s+e)//2
        if l[m]>=t:e=m-1
        else:s=m+1
    for y in [s-1,s,s+1]:
        if 0<=y<n and x!=y and ans[0]>abs(l[x]+l[y]):
            ans=[abs(l[x]+l[y]),l[x],l[y]]
print(*ans[1:])