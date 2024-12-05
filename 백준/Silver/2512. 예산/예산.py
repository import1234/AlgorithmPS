input()
n=list(map(int,input().split()))
M=int(input())
h=max(n)
l=0

def c(m):
    s=0
    for x in n:
        if x<m:s+=x
        else:s+=m
    return s

while h>l+1:
    m=(l+h)//2
    s=c(m)
    if s<M:l=m
    else:h=m
if c(h)<=M:print(h)
else:print(l)