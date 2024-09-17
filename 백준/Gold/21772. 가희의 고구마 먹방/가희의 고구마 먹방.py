m,n,t=map(int,input().split())
l=[]
for x in range(m):
    l+=[[*input()]]
    if 'G'in l[-1]:S=(x,l[-1].index('G'))
M=0
def f(x,y,route,count):
    global M,co
    if l[x][y]=="S" and (x,y) not in route:
        count+=1
    if len(route)==t:
        M=max(M,count)
        return
    for a,b in[(0,1),(0,-1),(1,0),(-1,0)]:
        if 0<=x+a<m and 0<=y+b<n and l[x+a][y+b]!="#":
            f(x+a,y+b,route+[(x,y)],count)
    return
f(S[0],S[1],[],0)
print(M)