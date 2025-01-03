n,k=map(int,input().split())
def f(x):print('YG'if x else'HS')
if n==1:
    if k%6==0 or k%6==5:f(0)
    else:f(1)
else:
    if k%6==1:f(0)
    else:f(1)