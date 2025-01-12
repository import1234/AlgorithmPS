n=int(input())
l=[*map(int,input().split())]

ans=[]
for x in range(n):
    s=0
    e=n-1
    t=-l[x]
    while s<=e:
        m=(s+e)//2
        if l[m]>=t:e=m-1
        else:s=m+1
    def f(a):
        if a<n and a!=x:ans.append([abs(l[x]+l[a]),l[x],l[a]])
    f(s);f(s+1);f(s-1)
print(*sorted(ans)[0][1:])