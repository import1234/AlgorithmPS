import sys
i=sys.stdin.readline
n,x=map(int,i().split())
l=[]
for _ in range(n+1):
    a,t=map(int,i().split())
    l.append(a)
ans=l[0]
for t in range(n):
    ans=x*ans+l[t+1]
    ans%=10**9+7
print(ans)