n1=int(input())
l1=[*map(int,input().split())]
n2=int(input())
l2=[*map(int,input().split())]

def f(a,b):
    if len(a)>len(b):a,b=b,a
    sa=sorted(a,reverse=1)
    sb=set(b)
    t=None
    for x in sa:
        if x in sb:
            t=x
            break
    if t:
        return [t]+f(a[a.index(t)+1:],b[b.index(t)+1:])
    else:
        return []

ans=f(l1,l2)
print(len(ans))
print(*ans)