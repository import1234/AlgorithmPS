r,c=map(int,input().split())
l=[[*map(lambda x:2**(ord(x)-65),input())]for x in' '*r]
t,C={(0,0,l[0][0])},0
while q:=t:
 t=set()
 for x,y,z in q:
  for a,b in[(1,0),(-2,0),(1,1),(0,-2)]:
   x+=a;y+=b
   if r>x>=0and c>y>=0and l[x][y]&z==0:t.add((x,y,z|l[x][y]))
 C+=1
print(C)