d={}
for x in[0]*int(input()):l=input().split();d[l[0]]=l[1:]
def f(x):
    if x=='.':return
    t=['f(d[x][0])','f(d[x][1])']
    t.insert(i,"print(x,end='')")
    exec(';'.join(t))
for i in range(3):f('A');print()