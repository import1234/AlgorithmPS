n=int(input())
l=[*map(int,input().split())]

def f(l,i):
    if i==0 or i==5:j=5-i
    elif 1<=i<=2:j=i+2
    else:j=i-2
    return [max(set(l)-{l[i],l[j]}),l[j]]

ans=[f(l,x)for x in range(6)]
for _ in range(n-1):
    l=[*map(int,input().split())]
    t=[[l[x]]+f(l,x)for x in range(6)]
    for x in range(6):
        p=[]
        for y in range(6):
            if ans[x][-1]==t[y][0]:p.append(t[y][1:])
        p.sort()
        ans[x].pop()
        ans[x].extend(p[-1])
print(max(sum(x[:-1])for x in ans))