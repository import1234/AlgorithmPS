n,m=map(int,input().split())
if n>=m:print(0);exit()
r=1
for x in range(1,n+1):r=r*x%m
print(r)