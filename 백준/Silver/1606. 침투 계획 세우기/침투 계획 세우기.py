n,m=map(int,input().split())
# c=1
# l=x=y=0
# if x==n and y==m:print(c);exit()
# while 1:
#     for i,j in [[-1,1],[-1,0],[0,-1],[1,-1],[1,0],[0,1]]:
#         for k in range(l - (1 if i==-1 and j==1 else 0)):
#             x+=i;y+=j;c+=1
#             if x==n and y==m:print(c);exit()
#     l+=1;y+=1;c+=1
#     if x==n and y==m:print(c);exit()
if n==0 and m==0:print(1);exit()

#겹 정하기
if n>=0:
    if m<-n:l=-m
    elif -n<=m<=0:l=n
    else:l=n+m
else:
    if m<0:l=-n-m
    elif 0<=m<=-n:l=-n
    else:l=m

x,y=l-1,1
c=3*(l-1)**2+3*(l-1)+1 +1 #(l-1, 1)에서의 좌표(l겹임)

if x==n and y==m:print(c);exit()
for i,j in [[-1,1],[-1,0],[0,-1],[1,-1],[1,0],[0,1]]:
    for k in range(l - (1 if i==-1 and j==1 else 0)):
        x+=i;y+=j;c+=1
        if x==n and y==m:print(c);exit()