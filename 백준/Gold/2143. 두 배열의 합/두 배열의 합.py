def f():
    l=[]
    n=int(input())
    t=[*map(int,input().split())]
    for x in range(n):
        i=0
        for y in range(x,n):
            l.append(i:=i+t[y])
    return l
T=int(input())
a,b=f(),f()
d={}
for x in b:d[x]=d.get(x,0)+1
print(sum(d.get(T-x,0)for x in a))