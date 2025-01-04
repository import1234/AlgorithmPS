e,C,*l=map(int,open(0).read().split())
l.sort()

def f(x):
    count=1
    t=l[0]
    for i in l:
        if i-t>=x:
            t=i
            count+=1
    return count>=C

s=0
e=10**9
while s<=e:
    mid=(s+e)//2
    if f(mid):s=mid+1
    else:e=mid-1
print(e)