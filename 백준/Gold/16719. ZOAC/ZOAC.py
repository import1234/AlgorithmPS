s=list(input())
n=len(s)
u=[0]*n
def f(a,b):
    if a>=b:return
    m=s[a:b].index(min(s[a:b]))+a
    u[m]=1
    print(''.join(s[x] if u[x]else'' for x in range(n)))
    f(m+1,b)
    f(a,m)
f(0,n)