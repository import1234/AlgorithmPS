count=0
s,p=map(int,input().split())
l=input()
A,C,G,T=map(int,input().split())
t=[0,0,0,0]
for x in range(p):
   t['ACGT'.index(l[x])]+=1
if all(t[y]>=[A,C,G,T][y] for y in range(4)):count+=1
for x in range(p,s):
   t['ACGT'.index(l[x])]+=1
   t['ACGT'.index(l[x-p])]-=1
   if all(t[y]>=[A,C,G,T][y] for y in range(4)):count+=1
print(count)