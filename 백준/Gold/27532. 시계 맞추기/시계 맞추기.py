n=int(input())
l=[]
for x in range(n):
    a,b=map(int,input().split(':'))
    l.append((a%12)*60+b)
a=n
for r in range(720):
    b=set()
    for x in range(n):
        if (l[x]-r*x)%720 not in b:
            b.add((l[x]-r*x)%720)
            if len(b)>a:break
    a=min(len(b),a)
print(a)