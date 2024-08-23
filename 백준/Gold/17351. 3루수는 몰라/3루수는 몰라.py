n=int(input())
l=[]
for x in range(n):
    l.append([*input()])

t={(0,0)}
while q:=t:
    t=set()
    for a,b in q:
        u=0
        u=max(u,l[a-1][b]//4*4 if a>0 else 0,l[a][b-1]//4*4 if b>0 else 0)
        if l[a][b]not in list('MOLA'):l[a][b]=u
        else:
            p=l[a][b]
            l[a][b]=u+(l[a][b]=='M')
            if a-1>=0 and l[a-1][b]%4=='MOLA'.find(p):l[a][b]=max(l[a][b],l[a-1][b]+1)
            if b-1>=0 and l[a][b-1]%4=='MOLA'.find(p):l[a][b]=max(l[a][b],l[a][b-1]+1)
        
        if a+1<n:t.add((a+1,b))
        if b+1<n:t.add((a,b+1))

#for x in l:print(*x)
print(l[-1][-1]//4)