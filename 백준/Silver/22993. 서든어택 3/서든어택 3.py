input()
a,*l=map(int,input().split())
l.sort()
for x in sorted(l):
    if a<=x:print('No');exit()
    a+=x
print('Yes')