s='YOKOHAMA'
n,m=map(int,input().split())
l=[input()for x in' '*n]
c=0
def f(x,y,i):
    if l[x][y]==s[i]:
        if i==7:
            global c
            c+=1
            return
        for a,b in [(0,1),(0,-2),(1,1),(-2,0)]:
            x+=a;y+=b
            if 0<=x<n and 0<=y<m:f(x,y,i+1)

for x in range(n):
    for y in range(m):f(x,y,0)
print(c)