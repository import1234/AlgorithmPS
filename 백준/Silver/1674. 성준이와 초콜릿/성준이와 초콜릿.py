q=[]
cho=[]
cof=[]
for x in open(0).read().split('\n'):
    if len(x)==0:continue
    if x[0]=='Q':
        q.append(int(x.split()[1]))
        continue
    x=x.split()
    t,n=int(x[1]),float(x[2])
    if x[0][1]=='h':
        cho.append((t,n))
    else:
        cof.append((t,n))


for T in sorted(q):
    r=0
    for t,n in cho:
        if T>=t:
            r+=max(8*n-(T-t)/12,0)
    for t,n in cof:
        if T>=t:
            r+=max(2*n-(T-t)**2/79,0)
    print(T,round(max(r,1)+10**-8,1))