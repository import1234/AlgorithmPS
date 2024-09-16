from itertools import combinations
n,m=map(int,input().split())
chickPos=[]
housePos=[]
l=[]
for x in range(n):
    l.append([*map(int,input().split())])
    for y in range(n):
        if l[x][y]==1:housePos.append([x,y])
        elif l[x][y]==2:chickPos.append([x,y])
matrix=[[0 for x in range(len(chickPos))]for y in range(len(housePos))]
for x in range(len(housePos)):
    for y in range(len(chickPos)):
        matrix[x][y]=abs(housePos[x][0]-chickPos[y][0])+abs(housePos[x][1]-chickPos[y][1])

result=float('inf')
for comb in combinations([i for i in range(len(chickPos))],m):
    cityDist=0
    for x in range(len(housePos)):
        minDist=float('inf')
        for y in comb:minDist=min(minDist,matrix[x][y])
        cityDist+=minDist
    result=min(result,cityDist)
print(result)