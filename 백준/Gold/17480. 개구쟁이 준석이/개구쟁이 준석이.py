n=int(input())
l=input().split()
d={}
for x in range(n):d[l[2*x]]=int(l[2*x+1])
l=[]
s=input()
n=len(s)
for x in range(n):
    for y in range(x+1,n+1):
        t={}
        for z in s[x:y]:t[z]=t.get(z,0)+1
        if d==t:l.append(s[x:y])

def f(x):
    n=len(x)
    if n==1:return x
    s=set()
    for n in [n//2,n//2+n%2]:
        a,b=x[:n],x[n:]
        for y in f(b):s.add(a[::-1]+y)
        for y in f(a):s.add(y+b[::-1])
    return s
        
s=set()
for x in l:
    for y in f(x):s.add(y)
print(len(s))