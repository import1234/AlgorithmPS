def f(x):return int(x[:2])*3600+int(x[3:5])*60+float(x[6:])
d1={};d2={}
for x in range(int(input())):
    a,b=map(f,input().split())
    if a in d1:d1[a].append(x)
    else:d1[a]=[x]
    if b in d2:d2[b].append(x)
    else:d2[b]=[x]
ans=bus=0
for t in sorted(set([*d1.keys()]+[*d2.keys()])):
    if t in d2:bus-=len(d2[t])
    if t in d1:bus+=len(d1[t])
    ans=max(ans,bus)
print(ans)