n=int(input())
a,b=1,0
while n:a,b=(a+b)%15746,a;n-=1
print(a)