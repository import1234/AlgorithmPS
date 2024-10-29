n=int(input())
d=[n*[0]for x in' '*n]
l=[[*map(int,input().split())]for x in' '*n]

for i in range(1,n):
    for x in range(n-i):
        d[x][x+i]=min(d[x][x+j]+d[x+j+1][x+i]+l[x][0]*l[x+j][1]*l[x+i][1]for j in range(i))

print(d[0][n-1])