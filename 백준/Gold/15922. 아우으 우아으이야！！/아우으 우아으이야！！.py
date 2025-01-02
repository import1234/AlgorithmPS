n=int(input())

t=0
s=e=None
for x in range(n):
    a,b=map(int,input().split())
    if s==None:
        s=a
        e=b
    if a<=e:
        e=max(e,b)
    else:
        t+=e-s
        s=a
        e=b
t+=e-s  
print(t)