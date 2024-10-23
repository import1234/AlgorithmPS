from math import gcd,lcm
p=[];q=[]
for x in' '*int(input()):
    a,b=map(int,input().split())
    g=gcd(a,b)
    p.append(a//g)
    q.append(b//g)

print(gcd(*p),lcm(*q))