n=int(input())
l=[]
xpos={}
ypos={}
for _ in range(n):
    x,y=map(int,input().split())
    l.append([x,y])
    if xpos.get(x):xpos[x].append(y)
    else:xpos[x]=[y]
    if ypos.get(y):ypos[y].append(x)
    else:ypos[y]=[x]
mx=min(xpos);my=min(ypos);Mx=max(xpos);My=max(ypos)
length=max(Mx-mx,My-my)
s=[1,1]
for x,y in l:
    if x in [mx,mx+length] or y in [my,my+length]:pass
    else:s[0]=0;break
for x,y in l:
    if x in [Mx-length,Mx] or y in [My-length,My]:pass
    else:s[1]=0;break
print(length if sum(s) else-1)