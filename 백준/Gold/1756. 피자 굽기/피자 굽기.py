d,n=map(int,input().split())
l=[*map(int,input().split())]
z=[*map(int,input().split())]
p=d+1
inf=float('inf')

M=inf
ml=[]
for x in range(d):
    if l[x]<M:
        M=l[x]
        ml.append((M,x+1))
ml.append((0,d+1))
ml.append((inf,0))
ml.sort()


def f(a):
    low=0
    high=len(ml)
    while low<=high:
        mid=(low+high)//2
        if ml[mid][0]==a:return ml[mid-1]
        elif ml[mid][0]<a:low=mid+1
        else:high=mid-1
    return ml[low-1]

for x in z:
    t=f(x)[1]-1
    p=min(p-1,t)
    if p<=0:print(0);exit()
print(p)