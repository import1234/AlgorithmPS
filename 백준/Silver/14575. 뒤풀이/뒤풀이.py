n,t=map(int,input().split())
l=[]
a=b=leftSum=rightSum=0
for x in range(n):
    left,right=map(int,input().split())
    l.append((left,right))
    leftSum+=left
    rightSum+=right
    a=max(left,a)
    b=max(right,b)

if not leftSum<=t<=rightSum:print(-1);exit()


def f(m):
    s=0
    for x,y in l:
        s+=min(m,y)
        if s>=t:return 1
    return 0

while a<b:
    m=(a+b)//2
    if f(m):b=m
    else:a=m+1

if b>a:a,b=b,a
if f(a):print(a)
else:print(b)