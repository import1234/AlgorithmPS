f=lambda:map(int,input().split())
n=sum(f())
l=[*f()]
t,p=f()
print(sum(1+(x-1)//t for x in l),n//p,n%p)