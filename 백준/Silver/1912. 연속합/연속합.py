n=int(input())
l=[*map(int,input().split())]
for x in range(1,n):l[x]=max(l[x]+l[x-1],l[x])
print(max(l))