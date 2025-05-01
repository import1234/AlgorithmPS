n,t,*l=map(int,open(0).read().split())
if t==1:
    k=int(*l)-1
    t=2
    l=[]
    while k:
        l.append(k%t)
        k//=t
        t+=1
    while len(l)!=n-1:l.append(0)
    s=[]
    a=[i for i in range(1,n+1)]
    for x in l[::-1]:s.append(a.pop(x))
    s.append(a.pop())
    print(*s)
else:
    a=[i for i in range(1,n+1)]
    t=[]
    for x in l[:-1]:
        t.append(a.index(x))
        a.pop(a.index(x))
    a=0
    k=2
    s=1
    for x in range(n-1):
        a+=t[-1-x]*s
        s*=k
        k+=1
    print(a+1)