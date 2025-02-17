a,b=map(int,input().split())
f=lambda a:str(a)if a>=0 else'('+str(a)+')'
g=lambda o:f(a)+o+f(b)
a=[(a+b,g('+')),(a-b,g('-')),(a*b,g('*'))]
a.sort(reverse=1)
if a[0][0]==a[1][0]:print('NIE')
else:print(a[0][1]+'='+f(a[0][0]))