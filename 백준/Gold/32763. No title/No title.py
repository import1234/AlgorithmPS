n=int(input())
l=[0]*n
a,b=[1],[];c=[a,b]
t=0
for x in range(n-1):
    print('?',x+1,'*',x+2)
    t^=input()=='-'
    l[x+1]=t
    c[t]+=[x+2]
if len(a)<2:a=b
print('?',a[0],'+',a[1])
v=input()=='-'
print('!',*['-'if v^x^l[a[0]-1]else'+'for x in l])