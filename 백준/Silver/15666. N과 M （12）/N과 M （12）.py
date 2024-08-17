from itertools import combinations_with_replacement as c
n,m=map(int,input().split())
l=[*map(int,input().split())]
r=[]
for x in c(l,m):r.append(tuple(sorted(list(x))))
for x in sorted(set(r)):print(*x)