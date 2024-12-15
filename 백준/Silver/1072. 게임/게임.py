x,y=map(int,input().split())
z=y*100//x
if z>=99:print(-1);exit()
c=0
while 1:
    c+=100000;y+=100000;x+=100000
    if y*100//x!=z:break

while y*100//x>z:c-=1;y-=1;x-=1
print(c+1)