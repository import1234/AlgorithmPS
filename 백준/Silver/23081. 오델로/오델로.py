n=int(input())
l=[input()for _ in range(n)]
result=[]
for x in range(n):
    for y in range(n):
        if l[x][y]!='.':continue
        count=0
        for a,b in[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            p,q=x,y
            for c in range(1,n):
                p+=a;q+=b
                if 0<=p<n and 0<=q<n:
                    if l[p][q]=='B':count+=c-1;break
                    elif l[p][q]=='.':break
                else:break
        if count:result+=[[count,y,x]]

if result:
    result.sort(key=lambda x:(-x[0],x[2],x[1]))
    print(*result[0][1:])
    print(result[0][0])
else:print('PASS')