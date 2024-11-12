n=int(input())
l=[]
for x in range(1,n+1):
    if n%x==0:l.append(x)
print(sum(l)*5-24)