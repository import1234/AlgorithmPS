l=[]
n=int(input())
for x in range(n//2):l+=[n-x,n+x+2]
if n%2==1:l[-1]+=n+1;l+=[0]
print(*l,n+1)