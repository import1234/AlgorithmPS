n,r=map(int,input().split())
m=1000000007

def f(a,k,m): #a^k 거듭제곱 구하기
    ans=1
    while k:
        if k%2==1:ans=(ans*a)%m
        a=(a*a)%m
        k>>=1
    return ans

a=1
for x in range(1,n+1):a=(a*x)%m
for x in range(1,r+1):a=(a*f(x,m-2,m))%m
for x in range(1,n-r+1):a=(a*f(x,m-2,m))%m
print(a)