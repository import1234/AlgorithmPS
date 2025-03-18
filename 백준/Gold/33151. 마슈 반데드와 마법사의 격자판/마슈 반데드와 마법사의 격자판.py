n,k=map(int,input().split())

if k<n*n//2:print(-1);exit()
l=[[0]*n for x in' '*n]
t=(k-n*n//2)//(n*n)
for x in range(n*n):l[x//n][x%n]=t
c=t*n*n+n*n//2

def f(a):
    global c
    if c==k:return
    for x in range(n):
        for y in range((x%2)^(1-a),n,2):
            l[x][y]+=2
            c+=2
            if c==k:return
    for x in range(n):
        for y in range((x%2)^a,n,2):
            l[x][y]+=2
            c+=2
            if c==k:return

def p():
    for x in l:print(*x)

if n%2:
    if (k%2)^(t%2):
        for x in range(n*n):
            l[x//n][x%n]+=1-x%2
        c+=1        
        f(0)
    else:
        for x in range(n*n):
            l[x//n][x%n]+=x%2
        f(1)
else:
    if k%2:print(-1);exit()
    else:
        for x in range(n*n):
            l[x//n][x%n]+=(x%2)^((x//n)%2)
        f(1)

p()