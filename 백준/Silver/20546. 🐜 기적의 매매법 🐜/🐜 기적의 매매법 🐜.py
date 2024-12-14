n=int(input())
l=[*map(int,input().split())]
J=[n,0]
S=[n,0]
for x in l:
    if J[0]>=x:
        c=J[0]//x
        J[0]-=c*x
        J[1]+=c

for x in range(3,len(l)):
    if l[x-3]>l[x-2]>l[x-1]>l[x]:
        c=S[0]//l[x]
        S[0]-=c*l[x]
        S[1]+=c
    if l[x-3]<l[x-2]<l[x-1]<l[x]:
        S[0]+=S[1]*l[x]
        S[1]=0

J=J[0]+J[1]*l[x]
S=S[0]+S[1]*l[x]
if J>S:print('BNP')
elif S>J:print('TIMING')
else:print('SAMESAME')