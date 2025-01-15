import sys
i=sys.stdin.readline
f=lambda:map(int,i().split())
n=int(*f())
l=[*f()]
dp=[[1]*(n) for x in' '*(n)]
for I in range(n):
    for p in range(n):
        if p+I<n:
            dp[p][p+I]=int(l[p]==l[p+I])
            if p+1<p+I-1:dp[p][p+I]*=dp[p+1][p+I-1]

# for x in dp:print(*x)

for x in' '*int(*f()):
    a,b=f()
    a-=1;b-=1
    print(dp[a][b])