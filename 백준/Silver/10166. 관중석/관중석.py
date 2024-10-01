from math import gcd
a,b=map(int,input().split())
l=set()
for x in range(a,b+1):
    for y in range(x):g=gcd(x,y);l.add(f'{y//g}/{x//g}')
print(len(l))