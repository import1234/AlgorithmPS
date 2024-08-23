n=int(input())
l,t=[],{(0,0)}
for x in'0'*n:l+=[[*input()]]
while q:=t:
    t=set()
    for a,b in q:
        u=max(l[a-1][b]//4*4if a else 0,l[a][b-1]//4*4if b else 0)
        if l[a][b]in'MOLA':
            p=l[a][b];l[a][b]=u+(l[a][b]=='M')
            for i in[0,1]:
                if[a,b][i]>0and l[a-~i%2][b-i]%4=='MOLA'.find(p):l[a][b]=max(l[a][b],l[a-~i%2][b-i]+1)
        else:l[a][b]=u
        if a+1<n:t.add((a+1,b))
        if b+1<n:t.add((a,b+1))
print(l[-1][-1]//4)