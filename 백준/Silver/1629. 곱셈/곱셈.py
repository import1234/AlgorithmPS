a,b,c=map(int,input().split())
l=[a]
o=bin(b)[2:][::-1]
for x in o:l.append(l[-1]**2%c)
r=1
for x in range(len(o)):r*=l[x]%c if o[x]=='1' else 1
print(r%c)