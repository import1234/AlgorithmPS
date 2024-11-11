def f(x):print(x);exit()
g=lambda:map(int,input().split())

n,m=g()
l=['X'*(m+2)]
l+=[[*'X'+input()+'X']for x in' '*n]+l
r1,c1=g();r2,c2=g()

t={(r1,c1,0)}
while q:=t:
    t=set()
    for x,y,z in q:
        for a,b in[(0,1),(0,-2),(1,1),(-2,0)]:
            x+=a;y+=b
            if l[x][y]!='X':
                t.add((x,y,z))
                l[x][y]='X'
            elif (x,y)==(r2,c2):
                if l[x][y]=='X':f('YES')
                if z:f('YES')
                else:t.add((x,y,1))
f('NO')