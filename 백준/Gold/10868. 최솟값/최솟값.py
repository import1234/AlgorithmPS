import sys
i=sys.stdin.readline
n,m=map(int,i().split())
l=[[int(i())for x in' '*n]]
while len(l[-1])!=1:
    t=[]
    for x in range(len(l[-1])//2):
        t.append(min(l[-1][2*x:2*x+2]))
    if len(l[-1])%2==1:t.append(l[-1][-1])
    l.append(t[::])

for _ in' '*m:
    a,b=map(int,i().split())
    a-=1;b-=1
    lt=l[0][a]
    rt=l[0][b]
    for x in range(len(l)-1):
        if a+1>=b:print(min(rt,lt));break
        if a%2==0 and a+1<len(l[x]):lt=min(lt,l[x][a+1])
        if b%2==1:rt=min(rt,l[x][b-1])
        a//=2
        b//=2
