import math,sys
i=sys.stdin.readline

n=int(i())
l={}
for _ in range(n):
    a,b=map(int,i().split())
    g=math.gcd(a,b)
    if g==0:g=1
    a//=g;b//=g
    if l.get((a,b)):l[(a,b)]+=1
    else:l[(a,b)]=1

r=0
for a,b in l:
    if a==0 and b==0:r+=l[(0,0)]**2-l[(0,0)]
    else:
        if l.get((b,-a)):r+=l[(a,b)]*l[(b,-a)]
        if l.get((-b,a)):r+=l[(a,b)]*l[(-b,a)]
        if l.get((0,0)):r+=2*l[(a,b)]*l[(0,0)]
print(r//2)