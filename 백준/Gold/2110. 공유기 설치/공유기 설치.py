_,C,*l=map(int,open(0).read().split())
l.sort()
def f(x):
    c,t=1,l[0]
    for i in l:
        if i-t>=x:t=i;c+=1
    return c>=C
s,e=0,10**9
while s<=e:
    m=(s+e)//2
    if f(m):s=m+1
    else:e=m-1
print(e)