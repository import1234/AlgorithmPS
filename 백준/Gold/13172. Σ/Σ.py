mod=10**9+7
def power(a,n):
    if n==0:return 1
    else:
        if n%2==1:return a*power(a,n-1)%mod
        else:return power(a,n//2)**2%mod

f=lambda b,a:a*power(b,mod-2)%mod

print(sum(f(*map(int,input().split()))for _ in' '*int(input()))%mod)