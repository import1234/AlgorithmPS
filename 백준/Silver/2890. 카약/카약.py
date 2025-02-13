n,m=map(int,input().split())
a=[]
for x in range(n):
    t=input()
    for d in range(m):
        try:
            a.append((d,int(t[m-1-d])))
            break
        except:pass


b={}
pv=0
i=0
for d,y in sorted(a):
    if d!=pv:
        pv=d
        i+=1
    b[y]=i
for x in range(1,10):print(b[x])