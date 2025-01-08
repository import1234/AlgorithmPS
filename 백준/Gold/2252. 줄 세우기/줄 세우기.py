from collections import defaultdict as dd
f=lambda:map(int,input().split())
n,m=f()
ind=dd(int)
d=dd(list)
l=[]
for x in' '*m:
    a,b=f()
    d[a].append(b)
    ind[b]+=1

t=set(range(1,n+1))
for x in ind:t.remove(x)

ans=[]
while q:=t.copy():
    for x in q:
        ans.append(x)
        t.remove(x)
        for y in d[x]:
            ind[y]-=1
            if ind[y]==0:t.add(y)

print(*ans)

# #검산용
# d={}
# for x in range(len(ans)):d[ans[x]]=x
# for x,y in l:
#     if d[x]>d[y]:
#         print('no')
#         break