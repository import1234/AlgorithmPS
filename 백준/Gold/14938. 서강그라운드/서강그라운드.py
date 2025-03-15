from collections import defaultdict as dd
f=lambda:map(int,input().split())
n,m,r=f()
p=[0]+[*f()]
d=dd(dict) #d[start][end] = distance
for x in range(r):
    a,b,l=f()
    d[a][b]=l
    d[b][a]=l

ans=[]
for s in range(1,n+1):
    t={(s,0)} # city number, distance
    v={}
    a=0
    while q:=t:
        t=set()
        for cur,dis in q: #current, distance
            if dis>m:continue
            if cur not in v:a+=p[cur]
            v[cur]=dis
            for nex in d[cur].keys(): #next
                if (nex not in v) or dis+d[cur][nex]<v[nex]:
                    t.add((nex,dis+d[cur][nex]))
    ans.append(a)

print(max(ans))