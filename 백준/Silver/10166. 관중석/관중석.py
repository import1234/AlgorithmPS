from math import gcd
a,b=map(int,input().split())
l=set()
count=0
for x in range(a,b+1):
    t=set()
    for y in range(x):
        g=gcd(x,y)
        if x//g not in l:
            t.add(x//g)
            count+=1
    l.update(t)
print(count)