m,n=map(int,input().split())
l=[[0]*n for _ in range(m)]
for x in range(int(input())):
    a,b=map(int,input().split())
    l[a-1][b-1]='X'
l[0][0]=1

for y in range(n):
    for x in range(m):
        if l[x][y]=='X':continue
        if y%2==0:d=[(0,-1),(-1,-1),(-1,0)]
        else:d=[(1,-1),(0,-1),(-1,0)]
        for a,b in d:
            if 0<=x+a<m and 0<=y+b<n:
                l[x][y]+=l[x+a][y+b]if l[x+a][y+b]!='X' else 0

print(l[-1][-1]%(10**9+7))