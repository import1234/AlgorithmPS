n,m=map(int,input().split())
l=sorted(map(int,input().split()))
v=[]
def f(t,n,m):
    if t>=m:print(*v);return
    for x in l:
        if x not in v:v.append(x);f(t+1,n,m);v.pop()
f(0,n,m)