n,m=map(int,input().split())
manitoOf=[0]*(n+1)
assign=[0]*(n+1)
for x in" "*m:
    a, b=map(int,input().split())
    manitoOf[a]=b
    assign[b]=a
s=int(input())
if manitoOf[s]!=0:print('NOJAM');exit()

avail=[]
for x in range(1,n+1):
    if assign[x]==0:avail.append(x)

if len(avail)==1:print('NOJAM')
elif len(avail)==2:
    a,b=avail
    if manitoOf[a]==0 or manitoOf[b]==0:print('NOJAM')
    else:print(2)
else:print(len(avail)-(assign[s]==0))