from math import ceil
n=int(input())
l=sorted(map(int,input().split()))

def f(i):
    c=0
    y=n-1
    for x in range(n):
        while x<y and l[x]+l[y]>i:y-=1
        c+=y-x if y>x else 0
    return c

k=ceil(n*(n-1)/4)
s,e=0,2*10**9
while s<=e:
    m=(s+e)//2
    if k<=f(m):e=m-1
    else:s=m+1
print(s)