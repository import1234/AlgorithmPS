input()
l=[*map(int,input().split())]
d={}
for x in l:
    if d.get(x):d[x]+=1
    else:d[x]=1
for x in sorted(d,reverse=1):
    if d[x]==x:print(x);exit()
if 0 in d:print(-1)
else:print(0)