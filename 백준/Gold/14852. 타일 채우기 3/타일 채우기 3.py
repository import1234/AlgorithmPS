n=int(input())
l=[1]+[0]*n
l[1]=2
mod=1000000007
t=0
for x in range(2,n+1):
    l[x]=2*l[x-1]+3*l[x-2]
    if x-3>=0:t+=l[x-3]
    l[x]+=2*t
    l[x]%=mod
print(l[-1])