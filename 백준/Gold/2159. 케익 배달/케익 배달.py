f=lambda:map(int,input().split())
n=int(*f())
a,b=f()
p=[[0,a,b]for _ in'mtblr']
for x in' '*n:
    a,b=f()
    d=[(a,b),(a,b+1),(a,b-1),(a-1,b),(a+1,b)]
    l=[]
    for x in range(5):
        t=[10**10]
        for y in range(5):
            a,b=d[x]
            t=min(t,[p[y][0]+abs(a-p[y][1])+abs(b-p[y][2]),a,b])
        l.append(t)
    p=l
print(min(p)[0])