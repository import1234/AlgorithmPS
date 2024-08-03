from math import log2
n=int(input())
l=[*map(int,input().split())]
a=dict()
for x in range(n):
    if a.get(l[x]):a[l[x]].append(x)
    else:a[l[x]]=[x]
d=int(input())
a[l[d]].remove(d)
c=0
q=a[-1]
while q:
    t=[]
    for x in q:
        if a.get(x):t+=a[x]
        else:c+=1
    q=t
print(c)