r1,c1,r2,c2=map(int,input().split())
r=r2-r1+1
c=c2-c1+1

l=[[0]*c for x in' '*r]


def f(r,c,t,d):
    if d==0 and c==t and abs(r)<=t:
        return r+t
    elif d==1 and r==-t and abs(c)<=t:
        return c+t
    elif d==2 and c==-t and abs(r)<=t:
        return t-r
    elif d==3 and r==t and abs(c)<=t:
        return t-c
    return 'e'



for x in range(r):
    for y in range(c):
        v=1
        t=0
        while not l[x][y]:
            for d in range(4):
                v+=2*t
                a=f(x+r1,y+c1,t,d)
                if a!='e':
                    l[x][y]=v-a
            t+=1

p=max(len(str(l[x][y]))for x in range(r)for y in range(c))

for x in range(r):
    for y in range(c):
        print(f'%{p}d' % l[x][y], end=' ')
    print()