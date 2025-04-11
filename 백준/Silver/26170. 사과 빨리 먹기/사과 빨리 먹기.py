l=[[*map(int,input().split())]for x in' '*5]
r,c=map(int,input().split())
v=set()
ans=99
def f(x,y,k,t):
    if l[x][y]==1:
        k+=1
        if k==3:
            global ans
            ans=min(ans,t)
            return
    v.add((x,y))
    for a,b in[(0,1),(0,-1),(1,0),(-1,0)]:
        if 0<=x+a<5 and 0<=y+b<5 and l[x+a][y+b]!=-1 and (x+a,y+b)not in v:f(x+a,y+b,k,t+1)
    v.remove((x,y))
f(r,c,0,0)
print(-1 if ans==99 else ans)