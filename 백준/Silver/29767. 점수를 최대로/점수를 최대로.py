n,k=map(int,input().split())
l=[*map(int,input().split())]
for x in range(1,n):l[x]+=l[x-1]
l.sort()
print(sum(l[-k:]))