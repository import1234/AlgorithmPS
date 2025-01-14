import sys
sys.setrecursionlimit(10**5)
i=sys.stdin.readline
f=lambda:map(int,i().split())
n,r,q=f()
d={}
for x in range(n-1):
    a,b=f()
    d.setdefault(a,[]).append(b)
    d.setdefault(b,[]).append(a)

ans={}
v=set()
def dfs(x):
    v.add(x)
    t=1
    for y in d.get(x,[]):
        if y not in v:
            t+=dfs(y)
    ans[x]=t
    return t

dfs(r)

# print(ans)

for x in range(q):
    print(ans[int(i())])