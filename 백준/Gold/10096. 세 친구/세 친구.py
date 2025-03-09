n=int(input())
if n%2==0:print('NOT POSSIBLE');exit()
l=input()
ans=set()
for x in range(n):
    a=l[:x]+l[x+1:]
    t=a[:n//2]
    if t==a[n//2:]:ans.add(t)
    if len(ans)>1:print('NOT UNIQUE');exit()
if ans:print(*ans)
else:print('NOT POSSIBLE')