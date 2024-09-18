a,b,x=map(int,input().split());x/=100
print(a*b/(x*min(a,b)+(1-x)*max(a,b)))