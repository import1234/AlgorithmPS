n=int(input())
l=[0]+[*map(int,input().split())]+[0]
d1=[0]*(n+1)
d2=d1[:]
for x in range(1,n+1):
    M=0
    for y in range(x):
        if l[y]<l[x] and M<d1[y]:M=d1[y]
    d1[x]=M+1
l.reverse()
for x in range(1,n+1):
    M=0
    for y in range(x):
        if l[y]<l[x] and M<d2[y]:M=d2[y]
    d2[x]=M+1
d2.reverse()
print(max(d1[1+x]+d2[x]-1 for x in range(n)))