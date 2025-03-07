n,a,*l=map(int,open(0).read().split())
for x in sorted(l):
    if a<=x:print('No');exit()
    a+=x
print('Yes')