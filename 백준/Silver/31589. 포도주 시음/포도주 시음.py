n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
a=[l.pop()]
for x in range((k-1)//2):
    a.append(l.pop()-l[x])
print(sum(a))