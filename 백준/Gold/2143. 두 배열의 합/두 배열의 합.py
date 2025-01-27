def f():
    l=[]
    n=int(input())
    t=[*map(int,input().split())]
    for x in range(n):
        i=0
        for y in range(x,n):
            i+=t[y]
            l.append(i)
    return l

T=int(input())
m,M=f(),f()
if len(m)>len(M):m,M=M,m

d={}
for x in M:d[x]=d.get(x,0)+1
l=sorted(d.keys())

ans=0
for x in m:
    s,e=0,len(l)-1
    while s<=e:
        m=(s+e)//2
        if l[m]==T-x:ans+=d[l[m]];break
        elif l[m]>T-x:e=m-1
        else:s=m+1
print(ans)