l=open(0).read().split()
t={(7,0)}
while q:=t:
 t=set()
 for x,y in q:
  if l[x][y]=='#':continue
  for a,b in[[0,0],[0,1],[-1,0],[0,-1],[0,-1],[1,0],[1,0],[0,1],[0,1]]:
   x+=a;y+=b
   if 0<=x<8and 0<=y<8and l[x][y]!='#':
    if(x,y)==(0,7):print(1);exit()
    t.add((x,y))
 l.insert(0,'0'*8)
print(0)