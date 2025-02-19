r,c=map(int,input().split())
f=lambda x:2**(ord(x)-65)
l=[[*map(f,input())]for x in' '*r]
t={(0,0,l[0][0])}
C=0
while q:=t:
    t=set()
    for x,y,z in q:
        for a,b in[(1,0),(-2,0),(1,1),(0,-2)]:
            x+=a;y+=b
            if 0<=x<r and 0<=y<c and l[x][y]&z==0:
                t.add((x,y,z|l[x][y]))
    C+=1
print(C)