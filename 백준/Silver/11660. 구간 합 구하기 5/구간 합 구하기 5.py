import sys
i=sys.stdin.readline
n,m=map(int,i().split())
l=[[0]+[0]*n]
for _ in[0]*n:
    l.append([0]+[*map(int,i().split())])
    for y in range(1,n+1):l[-1][y]+=l[-1][y-1]
    for y in range(n+1):l[-1][y]+=l[-2][y]
for x in[0]*m:
    a,b,c,d=map(int,i().split())
    print(l[c][d]-l[c][b-1]-l[a-1][d]+l[a-1][b-1])