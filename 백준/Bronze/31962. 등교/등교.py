f=lambda:map(int,input().split())
r=-1
n,x=f()
for _ in' '*n:
    s,t=f()
    if s+t<=x:r=max(r,s)
print(r)