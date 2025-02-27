a,b,c,i=map(int,input().split())
lim=10**18
l=set()
t={1}
while q:=t:
    t=set()
    for x in q:
        for y in [a,b,c]:
            if x*y<lim:
                l.add(x*y)
                t.add(x*y)

print(sorted(l)[i-1])