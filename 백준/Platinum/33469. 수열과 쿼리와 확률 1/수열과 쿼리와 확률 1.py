n,m=map(int,input().split())
input()
if input()=='S':print(1);exit()
mod=10**9+7
inv=lambda x:pow(x,mod-2,mod)
t=inv(2)
for x in range(1,n+1):t=(t*x*inv(n))%mod
t+=(n+1)*inv(4)
print(pow(t,m,mod))