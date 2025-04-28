n,r=map(int,input().split())
a,m=1,10**9+7
for x in range(r):a=(a*(n-x)*pow(r-x,m-2,m))%m
print(a)