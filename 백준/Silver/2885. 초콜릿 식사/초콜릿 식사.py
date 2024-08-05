from math import log2,ceil
k=int(input())
n=2**ceil(log2(k))
print(n)
c=0
while k>0:
    while k-n<0:n//=2;c+=1
    k-=n
print(c)