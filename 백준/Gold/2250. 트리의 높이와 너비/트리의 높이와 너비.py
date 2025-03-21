n=int(input())
v=set(range(1,n+1))
d={}
for x in range(n):
    a,b,c=map(int,input().split())
    v.discard(b)
    v.discard(c)
    d[a]=[b,c]
r=int(*v)

l={}

c=1
def dfs(r,level):
    global c
    a,b=d[r]
    if a!=-1:dfs(a,level+1)
    if level not in l:l[level]=[]
    l[level].append(c)
    c+=1
    if b!=-1:dfs(b,level+1)
            

dfs(r,1)
M=0
r=9**9
for x in l:
    t=l[x][-1]-l[x][0]+1
    if t>M:M=t;r=x
    elif t==M:r=min(r,x)
print(r,M)