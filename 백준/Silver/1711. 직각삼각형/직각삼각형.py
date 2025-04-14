i=[*map(int,open(0).read().split())]
n=i[0]
l=[(i.pop(),i.pop())for x in' '*n]
c=0
for x in range(n-2):
    for y in range(x+1,n-1):
        for z in range(y+1,n):
            (ax,ay),(bx,by),(cx,cy)=l[x],l[y],l[z]
            if (ax-cx)*(bx-cx)+(ay-cy)*(by-cy)==0 or \
                (ax-bx)*(cx-bx)+(ay-by)*(cy-by)==0 or \
                    (bx-ax)*(cx-ax)+(by-ay)*(cy-ay)==0:c+=1
print(c)