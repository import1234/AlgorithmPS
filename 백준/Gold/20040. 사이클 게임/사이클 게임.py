import sys
f=lambda:map(int,sys.stdin.readline().split())
n,m=f()
l=[*range(n)]
d=[1]*n

def r(a):
    if a!=l[a]:l[a]=r(l[a])
    return l[a]

for ans in range(m):
    a,b=f()
    ra,rb=r(a),r(b)
    if ra==rb:print(ans+1);exit()
    if d[ra]>d[rb]:d[ra]+=d[rb];l[rb]=l[ra]
    else:d[rb]+=d[ra];l[ra]=l[rb]
print(0)