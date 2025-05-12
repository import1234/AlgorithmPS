n=int(input())
l=set(map(int,input().split()))
m=max(l)

c=0
for x in l:
    k=0
    while 1:
        a=2*x*k+k**2
        if a in l:c+=1
        if a>m:break
        k+=1
print(c)