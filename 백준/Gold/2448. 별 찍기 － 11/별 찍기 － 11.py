from math import log2
n=int(input())
def f(k,n):
    l=[]
    if k==0:
        if n==1:
            l=['*','* *','*****']
        else:
            a=f(0,1)
            for x in range(3):l.append(a[x]+' '*(5-2*x)+a[x])
    else:
        if n==1:
            a=f(k-1,1)
            for x in range(3*2**(k-1)):l.append(a[x])
            b=f(k-1,2)
            for x in range(3*2**(k-1)):l.append(b[x])
        else:
            t=[]
            a=f(k-1,1)
            for x in range(3*2**(k-1)):t.append(a[x])
            b=f(k-1,2)
            for x in range(3*2**(k-1)):t.append(b[x])
            for x in range(3*2**k):l.append(t[x]+' '*(3*2**(k+1)-1-2*x)+t[x])
    return l

r=f(int(log2(n/3)),1)
for x in range(n):
    print(' '*(n-1-x)+''.join(r[x])+' '*(n-x))