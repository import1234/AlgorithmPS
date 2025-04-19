n,m,k=map(int,input().split())
s=set()
l=[]
for x in range(1,m+1):
    if x in s:continue
    l.append(x)
    s.add(x^k)
    if len(l)==n:print(*l);exit()
print(-1)