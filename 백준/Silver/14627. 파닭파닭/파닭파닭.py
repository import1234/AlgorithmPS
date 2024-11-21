S,C,*l=map(int,open(0).read().split())

s=0
e=10**9
while s<=e:
    m=(s+e)//2
    if m==0:break
    if sum(x//m for x in l)>=C:s=m+1
    else:e=m-1

print(sum(l)-e*C)