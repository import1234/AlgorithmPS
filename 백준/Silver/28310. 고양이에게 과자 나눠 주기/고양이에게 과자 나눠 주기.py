from fractions import Fraction
for t in' '*int(input()):
    n,m=map(int,input().split())
    N=[0]*n
    for x in' '*m:
        v,*a=map(int,input().split())
        for x in range(n):
            N[x]+=Fraction(a[x],v)
    print(max(N)-min(N))