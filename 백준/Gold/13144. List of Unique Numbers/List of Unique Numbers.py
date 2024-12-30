n=int(input())
l=[*map(int,input().split())]
d={}
c=t=m=0
for x in range(n):
    if l[x] in d and d[l[x]]>=m:
        t=x-d[l[x]]
        m=d[l[x]]
    else:
        t+=1
    c+=t
    d[l[x]]=x
print(c)