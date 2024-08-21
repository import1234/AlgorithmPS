def f(a,b):
    t=[[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            t[x][y]+=sum(a[x][z]*b[z][y]for z in range(n))
            t[x][y]%=1000
    return t

n,b=map(int,input().split())
l=[]
for x in'0'*n:l.append([*map(int,input().split())])
b=bin(b)[2:][::-1]
r=[[0]*x+[1]+[0]*(n-1-x)for x in range(n)]
M=[l]
for x in range(len(b)):
    M.append(f(M[-1],M[-1]))
    if b[x]=='1':r=f(r,M[x])
for x in r:print(*x)