n=int(input())
l=[*map(int,input().split())]

a,b=[],[]
for x in range(n):
    if x%2==0:a.append(l[x])
    else:b.append(l[x])
l.sort()
a.sort(reverse=1)
b.sort(reverse=1)

for x in range(n):
    if x%2==0:
        if l[x]!=a.pop():print('NO');exit()
    else:
        if l[x]!=b.pop():print('NO');exit()
print('YES')