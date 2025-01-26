from math import ceil
n,m=map(int,input().split())
l=[*map(int,input().split())]
for x in l:m-=x+1
if m<=0:
    print(0)
    exit()
a=[]
while 1:
    k=ceil(m/(n+1))
    a.append(k)
    m-=k
    n-=1
    if m<=0:break
ans=0
for x in a:
    for y in range(1,x+1):
        ans+=y**2
print(ans)
