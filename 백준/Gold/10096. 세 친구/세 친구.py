def f(a):print(a);exit()
n=int(input())
if n%2==0:f('NOT POSSIBLE')
l=input()
if len(set([*l]))==1:f(l[:n//2])

ans=set()
for x in range(n):
    a=0
    b=n//2
    if x<=n//2:b+=1
    t=[]
    yes=1
    for y in range(n//2):
        if a==x:a+=1
        if b==x:b+=1
        if l[a]==l[b]:t.append(l[a])
        else:yes=0;break
        a+=1
        b+=1
    if yes:
        ans.add(''.join(t))
        if len(ans)>1:f('NOT UNIQUE')
if ans:print(*ans)
else:f('NOT POSSIBLE')