from itertools import permutations as p
n=int(input())
l=[*map(int,input().split())]
for x in p(i+1 for i in range(n)):
    t=[0]*n
    for y in range(n):
        for z in range(y):
            if x[z]>x[y]:t[x[y]-1]+=1
    if t==l:
        print(*x)
        break