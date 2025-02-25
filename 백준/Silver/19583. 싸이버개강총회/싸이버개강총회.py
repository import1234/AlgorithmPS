f=lambda x:int(x[:2])*60+int(x[3:])
s,e,q=map(f,input().split())
d={}
while 1:
    try:t,a=input().split()
    except:break
    t=f(t)
    if a not in d:d[a]=[0,0]
    if t<=s:d[a][0]=1
    if e<=t<=q:d[a][1]=1
print(sum(sum(d[x])==2 for x in d))