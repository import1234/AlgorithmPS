n,m=map(int,input().split())
l=[['X']*(m+2)]+[list('X'+input()+'X')for x in range(n)]+[['X']*(m+2)]
r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
t={(r1,c1,0)}
while q:=t:
    t=set()
    for x,y,z in q:
        for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
            x+=a;y+=b
            if l[x][y]!='X':
                t.add((x,y,z))
                l[x][y]='X'
            elif (x,y)==(r2,c2):
                if l[x][y]=='X':print('YES');exit()
                if z:print('YES');exit()
                else:t.add((x,y,1))
print('NO')