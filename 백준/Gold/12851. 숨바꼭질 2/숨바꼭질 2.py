a,b=map(int,input().split())
lim=150001
v=[0]*lim
v[a]=1
if b<=a:print(a-b,1);exit()
q={a}
count=0
while v[b]==0:
    t=set()
    d={}
    for x in q:
        if 2*x<lim:
            if v[2*x]==0:t.add(2*x)
            d[2*x]=d.get(2*x,0)+v[x]
        if x+1<lim:
            if v[x+1]==0:t.add(x+1)
            d[x+1]=d.get(x+1,0)+v[x]
        if 0<=x-1:
            if v[x-1]==0:t.add(x-1)
            d[x-1]=d.get(x-1,0)+v[x]
    for x in d:v[x]+=d[x]
    q=t
    count+=1
print(count)
print(v[b])