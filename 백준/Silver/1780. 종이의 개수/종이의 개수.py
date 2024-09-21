n=int(input())
l=[[*map(int,input().split())] for x in range(n)]


d={-1:0,0:0,1:0}

def f(l):
    n=len(l)
    if n==1:d[l[0][0]]+=1;return
    t=l[0][0]
    for x in range(n):
        for y in range(n):
            if t!=l[x][y]:
                n//=3
                for i in range(3):
                    for j in range(3):
                        newl=[[0]*n for x in range(n)]
                        for x in range(n):
                            for y in range(n):
                                newl[x][y]=l[i*n+x][j*n+y]
                        f(newl)
                return
    d[l[0][0]]+=1
f(l)
for x in d:print(d[x])