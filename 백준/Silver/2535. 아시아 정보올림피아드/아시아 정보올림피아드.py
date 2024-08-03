l=sorted([[*map(int,input().split())]for _ in range(int(input()))],key=lambda x:x[2])
f=lambda:l.pop()[:2];a,b=f(),f();p=print;p(*a,*b)
if a[0]==b[0]:
 while (c:=f())[0]==a[0]:pass
 p(*c)
else:p(*f())