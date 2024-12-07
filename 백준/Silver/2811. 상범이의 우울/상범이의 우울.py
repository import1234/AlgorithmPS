n=int(input())+1
l=[*map(int,input().split())]+[0]
a=[0]*n
s=-1
M=0
d={}
for x in range(n):
    if l[x]<0:
        if s<0:s=x
    elif s>=0:
        d[x]=x-s
        M=max(M,d[x])
        s=-1

for x in d:
    s=x-3*d[x]
    c=0
    while s<x-d[x]:
        # print(s, s<x-d[x],x,d[x],x-d[x])
        if s>=0 and a[s]==0:a[s]=1
        s+=1

# print(d)
# print(a)

t=[0]
for x in d:
    if d[x]!=M:continue
    s=x-4*d[x]
    c=0
    while s<x-d[x]:
        if s>=0 and a[s]==0:c+=1
        s+=1
    t.append(c)

print(sum(a)+max(t))