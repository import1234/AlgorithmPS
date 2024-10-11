n=int(input())
l=[*map(int,input().split())]
r=[]
for x in range(n):r.append((l[x],x))
s=sorted(r,reverse=1)
ans=0
p=0
for x in s:
    a,b=x
    if b<p:continue
    for y in range(p,b):
        ans+=a-l[y]
    p=b+1
print(ans)