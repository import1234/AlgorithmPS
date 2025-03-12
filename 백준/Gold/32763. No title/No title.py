n=int(input())
l=[0]*n
a,b=[1],[]
c=[a,b]
t=0
for x in range(n-1):
    print(f"? {x+1} * {x+2}",flush=1)
    if'-'==input():t^=1
    l[x+1]=t
    c[t]+=[x+2]
if len(a)<2:a=b
print(f"? {a[0]} + {a[1]}",flush=1)
v=1
if(input()=='-')^l[a[0]-1]:v=0
print('! '+' '.join('+'if v^x else '-' for x in l),flush=1)