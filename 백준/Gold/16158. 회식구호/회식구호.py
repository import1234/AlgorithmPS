from math import gcd
N,X,K=map(int,input().split())
l=[*map(int,input().split())]
s=lambda x:x if x[-2:]!='/1'else x[:-2]
def f(p):
    n1=X*p;d=100;g1=gcd(n1,d);n2=200*p-n1;g2=gcd(n2,d);s1=f'{n1//g1}/{d//g1}';s2=f'{n2//g2}/{d//g2}'
    return n1/d,s(s1),n2/d,s(s2)
r=[*map(f,l)]
l=set();d={};e={}
for x in r:
    l.add(x[:2]);l.add(x[2:])
    d[x[0]]=d.get(x[0],0)+1
    e[x[2]]=e.get(x[2],0)-1
l=sorted(l)
c=0
for x in l:
    c+=d.get(x[0],0)
    if c>=K:print(x[1]);exit()
    c+=e.get(x[0],0)
print(-1)