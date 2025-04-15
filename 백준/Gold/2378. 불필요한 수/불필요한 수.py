n,m=map(int,input().split())
d={}

#m 소인수분해 하기
for x in range(2,int(m**.5)+1):
    while m%x==0:
        d[x]=d.get(x,0)+1
        m//=x
if m>1:d[m]=d.get(m,0)+1

def fac(n,p): #n!에 소수 p가 몇 번 등장하는지 세기
    a=0
    t=p
    while t<=n:
        a+=n//t
        t*=p
    return a

def com(n,k,p): #n choose k에 소수 p가 몇 번 등장하는지 세기
    return fac(n,p)-fac(k,p)-fac(n-k,p)

l=[]
for x in range(n):
    t={}
    for p in d:t[p]=com(n-1,x,p)
    if all(t[p]>=d[p] for p in d):l.append(x+1) #이항계수가 m으로 나누어 떨어지면 append
print(len(l))
print(*l)