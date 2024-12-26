n,k=map(int,input().split())
l=[*map(int,input().split())]

c=0
for x in range(n//2):
    a=l[x]
    b=l[n-1-x]
    a,b=max(a,b),min(a,b)
    t=(a-b)//k
    b+=t*k
    c+=t+min(a-b,b+k-a+1)
print(c)