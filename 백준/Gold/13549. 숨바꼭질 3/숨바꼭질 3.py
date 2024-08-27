inf=float('inf')
n,k=map(int,input().split())
if k<=n:print(n-k);exit()
q=[k]
l=[inf]*200001
l[k]=0

while l[n]==inf:
    t=set()
    for x in q:
        if x%2==0:t.add(x//2);l[x//2]=l[x]if l[x]<l[x//2]else l[x//2]
        if x+1<2*k and l[x+1]==inf:t.add(x+1);l[x+1]=1+l[x]if l[x]+1<l[x+1]else l[x+1]
        if x>0 and l[x-1]==inf:t.add(x-1);l[x-1]=1+l[x]if l[x]+1<l[x-1]else l[x-1]
    q=t
print(l[n])