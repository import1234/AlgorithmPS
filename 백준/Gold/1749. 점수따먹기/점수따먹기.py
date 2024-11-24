m,n=map(int,input().split())
l=[[*map(int,input().split())]for x in' '*m]

def f(l):
    a=0
    return max([a:=max(x,a+x) for x in l])

a=[]
for x in range(len(l)):
    t=[0]*len(l[0])
    for y in l[x:]:
        t=[sum(z) for z in zip(t,y)]
        a.append(f(t))
print(max(a))