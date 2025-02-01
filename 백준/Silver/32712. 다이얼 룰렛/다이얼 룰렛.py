f=lambda:map(int,input().split())
n,k=f()
l=[*f()]
M=0
for _ in'  ':
    r=[0]
    for x in range(min(n,k)):
        r.append(r[-1]+l[x])
        M=max(M,r[x+1]+(k-x-1)*l[x])
    l.reverse()
print(M)