def f(x):return int(x[:2])*3600+int(x[3:5])*60+float(x[6:])
d1={}
d2={}
for x in range(int(input())):
    a,b=map(f,input().split())
    if a in d1:d1[a].append(x)
    else:d1[a]=[x]
    if b in d2:d2[b].append(x)
    else:d2[b]=[x]
ans=0
bus=set()
for t in sorted(set([*d1.keys()]+[*d2.keys()])):
    if t in d2:
        for x in d2[t]:bus.remove(x)
    if t in d1:
        for x in d1[t]:bus.add(x)
    ans=max(ans,len(bus))
print(ans)