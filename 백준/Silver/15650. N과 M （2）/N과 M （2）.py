from itertools import combinations as c
n,m=map(int,input().split())
for x in c([i+1 for i in range(n)],m):print(*x)