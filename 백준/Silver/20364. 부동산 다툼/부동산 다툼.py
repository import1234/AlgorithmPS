import sys
i=sys.stdin.readline
n,q=map(int,input().split())
d={}
for x in range(q):
    o=x=int(i())
    y=0
    while x:
        if x in d:y=x
        x//=2
    if y==0:d[o]=1
    print(y)