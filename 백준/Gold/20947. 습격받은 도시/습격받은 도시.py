from collections import defaultdict as d
n=int(input())
dx=d(list)
dy=d(list)
wreck=[] #잔해
l=[]
for x in range(n):
    l+=[[*input()]]
    for y in range(n):
        if l[x][y]=='X':wreck+=[(x,y)]
        if l[x][y]!='.':dx[x]+=[y];dy[y]+=[x]

for x in dx:dx[x]=[-1]+dx[x]+[n]
for y in dy:dy[y]=[-1]+dy[y]+[n]

def binsearch(li,n): #len(li)>=2일 때만 실행가능, n과 가장 붙어있는 li[l]<n<li[h]인 l,h 반환
    low=0
    high=len(li)-1
    while low+1!=high:
        m=(low+high)//2
        if n<li[m]:high=m
        else:low=m
    return low,high
        

def check(x,y):
    #check horizontally
    horOkay=0

    if len(dx[x])==0:horOkay=1
    else:
        low,high=binsearch(dx[x],y)
        if dx[x][low]==-1 and dx[x][high]==n:horOkay=1
        elif dx[x][low]==-1:horOkay=l[x][dx[x][high]]=='X'
        elif dx[x][high]==n:horOkay=l[x][dx[x][low]]=='X'
        else:horOkay=l[x][dx[x][low]]=='X' and l[x][dx[x][high]]=='X'

    if horOkay==0:return 0

    #check vertically
    verOkay=0

    if len(dy[y])==0:verOkay=1
    else:
        low,high=binsearch(dy[y],x)
        if dy[y][low]==-1 and dy[y][high]==n:verOkay=1
        elif dy[y][low]==-1:verOkay=l[dy[y][high]][y]=='X'
        elif dy[y][high]==n:verOkay=l[dy[y][low]][y]=='X'
        else:verOkay=l[dy[y][low]][y]=='X' and l[dy[y][high]][y]=='X'

    if verOkay==0:return 0
    else:return 1

for wx,wy in wreck:
    # print('wreck:',wx,wy)
    dist=1
    br=0
    dirtoggle=[1,1,1,1]
    while 1:
        dirlist=[[0,dist],[0,-dist],[dist,0],[-dist,0]]
        # print(dirtoggle)
        for i in range(len(dirlist)):
            if dirtoggle[i]==0:continue
            a,b=dirlist[i]
            if 0<=wx+a<n and 0<=wy+b<n:
                # print(wx+a,wy+b)
                if l[wx+a][wy+b]not in['.','B']:
                    # print(l[wx+a][wy+b],wx+a,wy+b)
                    dirtoggle[i]=0
                elif check(wx+a,wy+b):
                    # print('check')
                    l[wx+a][wy+b]='B'
                    br=1
                    break
        dist+=1
        if dist==10:exit()
        if br:break

for x in l:print(''.join(x))

# 체크용(이거 해서 입력과 똑같이 나오면 성공)
# for x in range(n):
#     for y in range(n):
#         if l[x][y]=='X':l[x][y]='O'

# bomb=[]
# for x in range(n):
#     for y in range(n):
#         if l[x][y]=='B':bomb+=[(x,y)]

# for x,y in bomb:
#     l[x][y]='.'
#     a=x;b=y
#     for d in range(n):
#         x+=1
#         if not(0<=x<n and 0<=y<n):break
#         if l[x][y]in'OX':l[x][y]='X';break
#     x=a;y=b
#     for d in range(n):
#         x-=1
#         if not(0<=x<n and 0<=y<n):break
#         if l[x][y]in'OX':l[x][y]='X';break
#     x=a;y=b
#     for d in range(n):
#         y+=1
#         if not(0<=x<n and 0<=y<n):break
#         if l[x][y]in'OX':l[x][y]='X';break
#     x=a;y=b
#     for d in range(n):
#         y-=1
#         if not(0<=x<n and 0<=y<n):break
#         if l[x][y]in'OX':l[x][y]='X';break

# print(n)
# for x in l:
#     print(''.join(x))