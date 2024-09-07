from collections import defaultdict
f=lambda:map(int,input().split())
n,edges=f()
d=defaultdict(dict)
for x in'0'*edges:a,b,c=f();d[a][b]=c;d[b][a]=c
v1,v2=f()

def f(k,e):
    V={k:0}
    S={}
    while 1:
        for x in d[k]:
            if x in V:continue
            if x in S:S[x]=min(S[x],V[k]+d[k][x])
            else:S[x]=V[k]+d[k][x]
        if e in V:break

        m=float('inf')
        for x in S:
            if S[x]<m:m=S[x];k=x
        V[k]=m
        del S[k]
    return V[e]

try:a=f(1,v1)+f(v1,v2)+f(v2,n)
except:a=-1
try:b=f(1,v2)+f(v2,v1)+f(v1,n)
except:b=-1
if a==-1:print(b)
elif b==-1:print(a)
else:print(min(a,b))
