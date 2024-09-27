l=[[*input()]for x in range(8)]

t={(7,0)}
while q:=t:
    t=set()
    for x,y in q:
        if l[x][y]=='#':continue
        for a,b in[[0,0],[0,1],[-1,0],[0,-1],[0,-1],[1,0],[1,0],[0,1],[0,1]]:
            x+=a;y+=b
            if 0<=x<8 and 0<=y<8 and l[x][y]!='#':
                if (x,y)==(0,7):print(1);exit()
                t.add((x,y))
    l.pop()
    l.insert(0,[0]*8)

print(0)