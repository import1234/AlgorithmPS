import math
input()
c=[]
l=[]
for x in input().replace('long','$')+'.':
    if x=='$':l.append(1)
    else:
        if l:
            c.append(len(l))
            l=[]
a=1
for x in c:
    t=0
    for y in range(x):
        if x-y>=y:
            t+=math.comb(x-y,y)
    a*=t
print(a)
