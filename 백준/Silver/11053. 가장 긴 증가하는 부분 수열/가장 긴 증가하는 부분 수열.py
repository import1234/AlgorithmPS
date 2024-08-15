n=int(input())
l=[0]+[*map(int,input().split())]
d=[0]*(n+1)
for x in range(1,n+1):
    M=0;i=0
    for y in range(x):
        if l[y]<l[x] and M<d[y]:M=d[y];i=y
    d[x]=d[i]+1
print(max(d))