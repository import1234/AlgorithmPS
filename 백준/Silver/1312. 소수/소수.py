a,b,n=map(int,input().split())
while 1:
    a=a%b;a*=10;n-=1
    if n==0:print(a//b);break