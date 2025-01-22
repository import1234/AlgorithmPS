l=[]
for x in range(9):
    l.append([*input()])
r=[str(x)for x in range(1,10)]
v=[set(r)for x in' '*9] #세로
h=[set(r)for x in' '*9] #가로
s=[set(r)for x in' '*9] #네모

def nemoIdx(x,y):
    return 3*(x//3)+y//3

for x in range(9):
    for y in range(9):
        if l[x][y]=='0':continue
        h[x].remove(l[x][y])
        v[y].remove(l[x][y])
        s[nemoIdx(x,y)].remove(l[x][y])


def dfs(i):
    if i==81:
        for x in range(9):print(''.join(l[x]))
        exit()
    
    x=i//9
    y=i%9
    if l[x][y]=='0':
        t=h[x].intersection(v[y]).intersection(s[nemoIdx(x,y)])
        for z in sorted(t):
            l[x][y]=z
            h[x].remove(z);v[y].remove(z);s[nemoIdx(x,y)].remove(z)
            dfs(i+1)
            l[x][y]='0'
            h[x].add(z);v[y].add(z);s[nemoIdx(x,y)].add(z)
    else:
        dfs(i+1)

dfs(0)