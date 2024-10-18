n,t=map(int,input().split())
li=[]
a=b=sumL=sumR=0
for x in range(n):
    l,r=map(int,input().split())
    li.append(r)
    sumL+=l
    sumR+=r
    a=max(l,a)
    b=max(r,b)

if not sumL<=t<=sumR:
    print(-1)
    exit()

def f(m):
    s=0
    for y in li:
        s+=min(m,y)
        if s>=t:return 1
    return 0

while a<b:
    m=(a+b)//2
    if f(m):b=m
    else:a=m+1

print(a)