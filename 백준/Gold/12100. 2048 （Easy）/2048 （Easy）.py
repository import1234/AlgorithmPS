from copy import deepcopy
n=int(input())
l=[]
for x in range(n):
    l.append([*map(int,input().split())])

def rotateR(l):
    a=[[0]*n for x in' '*n]
    for x in range(n):
        for y in range(n):
            a[y][n-1-x]=l[x][y]
    return a

def rotateL(l):
    a=[[0]*n for x in' '*n]
    for x in range(n):
        for y in range(n):
            a[n-1-y][x]=l[x][y]
    return a

def moveL(l):
    l=deepcopy(l)
    t=[[0]*n for x in' '*n]
    for x in range(n):
        for y in range(n):
            while 1:
                if y<=0 or (l[x][y-1] not in [0,l[x][y]]):break
                if l[x][y-1]==0:
                    l[x][y-1]=l[x][y]
                    l[x][y]=0
                elif l[x][y-1]==l[x][y] and t[x][y-1]==0 and t[x][y]==0:
                    t[x][y-1]=1
                    l[x][y-1]*=2
                    l[x][y]=0
                y-=1
    return l

L=lambda l:moveL(l)
U=lambda l:rotateR(moveL(rotateL(l)))
R=lambda l:rotateR(rotateR(moveL(rotateR(rotateR(l)))))
D=lambda l:rotateL(moveL(rotateR(l)))
ans=0

def P(l):
    for x in l:print(*x)

def do(l,i,s):
    global ans
    if i==0:
        for x in range(n):
            for y in range(n):
                ans=max(ans,l[x][y])
    else:
        t=L(l) #왼쪽 이동
        do(t,i-1,'L'+s)
        t=U(l) #위 이동
        do(t,i-1,'U'+s)
        t=R(l) #오른쪽 이동
        do(t,i-1,'R'+s)
        t=D(l) #아래 이동
        do(t,i-1,'D'+s)

do(l,5,'')
print(ans)