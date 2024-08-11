import sys
i=sys.stdin.readline
for _ in range(int(i())):
    n,k=map(int,i().split())
    l=i().split()
    d={}
    for x in range(n):
        t=''.join(sorted(l[x].lower())) + str(sum(l[x][i].isupper() for i in range(k)))
        if d.get(t):d[t]+=1
        else:d[t]=1
    s=0
    for x in d.values():s+=x*(x-1)//2
    print(s)