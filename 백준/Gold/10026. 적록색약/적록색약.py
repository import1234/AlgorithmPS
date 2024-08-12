import sys
sys.setrecursionlimit(10**5)
n=int(input())
l=''
for _ in range(n):l+=input()
k=l.replace('R','G')
def f(a,b):
    t=l[a*n+b];l[a*n+b]='X'
    for x,y in[[a-1,b],[a+1,b],[a,b-1],[a,b+1]]:
        if 0<=x<n and 0<=y<n and l[x*n+y]==t:f(x,y)
for t in[l,k]:
    l=list(t)
    c=0
    for x in range(n*n):
        if l[x]!='X':f(x//n,x%n);c+=1
    print(c)