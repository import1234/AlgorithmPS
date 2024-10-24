import sys
i=sys.stdin.readline
d={}
f=lambda x:d.get(x,0)
for _ in' '*int(i()):
    q,r=map(int,i().split())
    if q==1:
        p=max(f(r+x)for x in range(4))
        for x in range(4):d[r+x]=p+1
    elif q==2:d[r]=f(r)+4
    else:print(f(r))