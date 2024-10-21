n,p=map(int,input().split())
v={n}
prev=n
while 1:
    now=prev*n%p
    if now in v:break
    v.add(now)
    prev=now

loop=prev=now
count=0
while 1:
    count+=1
    now=prev*n%p
    if now==loop:break
    prev=now
print(count)