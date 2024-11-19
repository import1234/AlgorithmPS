from itertools import permutations as p
l=[1]*10**7
l[0]=l[1]=0
for x in range(2,int(10**3.5)+1):
    if l[x]==0:continue
    y=x*x
    while y<10**7:
        l[y]=0
        y+=x

primes=set()
for x in range(10**7):
    if l[x]:
        primes.add(x)

def f(x,t):
    t=t*10+a[x]
    if t in primes:s.add(t)
    for y in range(len(a)):
        if v[y]==1:continue
        v[y]=1
        f(y,t)
        v[y]=0
    

for x in range(int(input())):
    a=[*map(int,list(input()))]
    v=[0]*len(a)
    s=set()
    for y in range(len(a)):
        v[y]=1
        f(y,0)
        v[y]=0
    
    print(len(s))