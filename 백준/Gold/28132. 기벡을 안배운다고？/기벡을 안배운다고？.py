import math
n,r,l=int(input()),0,{}
for _ in '1'*n:
 a,b=map(int,input().split());g=math.gcd(a,b)
 if g==0:g=1
 a//=g;b//=g;l[(a,b)]=1+l[(a,b)]if l.get((a,b))else 1
for a,b in l:
 t=l[(a,b)]
 if a==0 and b==0:r+=t*t-t
 else:
  if l.get((b,-a)):r+=t*l[(b,-a)]
  if l.get((-b,a)):r+=t*l[(-b,a)]
  if l.get((0,0)):r+=2*t*l[(0,0)]
print(r//2)