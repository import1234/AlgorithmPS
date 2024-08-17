a,b=map(int,input().split())
t={a}
c=0
while q:=t:
    c+=1
    t=set()
    for x in q:
        if x==b:print(c);exit()
        if 2*x<=b:t.add(2*x)
        if 10*x+1<=b:t.add(10*x+1)
print(-1)