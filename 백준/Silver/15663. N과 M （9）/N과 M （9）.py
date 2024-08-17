from itertools import permutations as p

n,m=map(int,input().split())
l=sorted(map(int,input().split()))
s=set()
for x in p(l,m):
    if x not in s:
        print(*x)
        s.add(x)