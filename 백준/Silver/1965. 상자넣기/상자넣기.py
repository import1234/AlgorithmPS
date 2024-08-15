n=int(input())
l=[0]+[*map(int,input().split())]
d={0:0}
for x in range(1,n+1):
    M=0
    for y in [*d.keys()]:
        if y<l[x] and d[y]>=M:M=d[y]
    d[l[x]]=M+1
print(max(d.values()))