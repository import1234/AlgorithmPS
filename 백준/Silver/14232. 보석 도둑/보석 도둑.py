k=int(input())
l=[]
for x in range(2,int(k**.5)+1):
    while k%x==0:
        l.append(x)
        k//=x
if k!=1:l.append(k)
print(len(l))
print(*l)