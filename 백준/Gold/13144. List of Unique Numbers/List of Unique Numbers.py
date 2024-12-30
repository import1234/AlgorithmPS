n,*l=map(int,open(0).read().split())
d={}
c=t=m=0
for x in range(n):
    if l[x] in d and d[l[x]]>=m:
        m=d[l[x]]
        t=x-m
    else:t+=1
    c+=t
    d[l[x]]=x
print(c)