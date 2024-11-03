n,*l=map(int,open(0).read().split())
p=-1
for x in range(n):
 if(p:=max(p+1,min(t:=l[x::n])))>max(t):print('NO');exit()
print('YES')