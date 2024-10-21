n,p=map(int,input().split())
l=[n]
prev=n
for x in range(1,1000):
    now=prev*n%p
    if now in l:break
    l.append(now)
    prev=now
print(x-l.index(now))