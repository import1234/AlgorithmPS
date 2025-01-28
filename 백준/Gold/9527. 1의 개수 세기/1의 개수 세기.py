f=lambda n:int(n*2**(n-1))
a,b=map(int,input().split())
def g(x):
    t=0
    x=bin(x)[2:]
    ans=0
    for y in range(len(x)):
        if x[y]=='1':
            ans+=t*2**(len(x)-y-1)+f(len(x)-y-1)+1
            t+=1
    return ans

print(g(b)-g(a-1))