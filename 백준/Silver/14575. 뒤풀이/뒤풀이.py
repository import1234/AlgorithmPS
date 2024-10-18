n,t,*l=map(int,open(0).read().split())
a,b=max(l[::2]),max(l[1::2])
if not sum(l[::2])<=t<=sum(l[1::2]):print(-1);exit()
while a<b:
    m=(a+b)//2
    if sum(min(m,x)for x in l[1::2])>=t:b=m
    else:a=m+1
print(a)