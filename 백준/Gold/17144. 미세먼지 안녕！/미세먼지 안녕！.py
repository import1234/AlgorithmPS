import copy
f=lambda:map(int,input().split())
r,c,T=f()
l=[[*f()]for x in' '*r]
air=[]
for x in range(r):
    if l[x][0]==-1:air+=[x]
a,b=air

for _ in' '*T:
    t=[[0]*c for x in' '*r]
    for x in range(r):
        for y in range(c):
            if l[x][y]>0:
                t[x][y]+=l[x][y]
                m=int(l[x][y]/5)
                for p,q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if 0<=p<r and 0<=q<c and not l[p][q]==-1:
                        t[x][y]-=m
                        t[p][q]+=m
            if l[x][y]==-1:t[x][y]=-1
    l=copy.deepcopy(t)
    #위
    for x in range(a-1,-1,-1):l[x+1][0]=l[x][0]
    for y in range(1,c):l[0][y-1]=l[0][y]
    for x in range(1,a+1):l[x-1][-1]=l[x][-1]
    for y in range(c-1,0,-1):l[a][y]=l[a][y-1]
    l[a][1]=0
    #아래
    for x in range(b,r-1):l[x][0]=l[x+1][0]
    for y in range(1,c):l[-1][y-1]=l[-1][y]
    for x in range(r-1,b,-1):l[x][-1]=l[x-1][-1]
    for y in range(c-1,0,-1):l[b][y]=l[b][y-1]
    l[b][1]=0
    l[a][0]=-1
    l[b][0]=-1

print(sum(l[x][y]for x in range(r) for y in range(c))+2)