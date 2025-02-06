a,b=map(int,input().split())
n=int(b**.5)+1
l=[1]*n
p=[]
for x in range(2,n):
    if l[x]==0:continue
    p.append(x)
    for y in range(x*x,n,x):l[y]=0

c=0
for x in p:
    t=x*x
    while t<=b:
        if a<=t:c+=1
        t*=x
print(c)