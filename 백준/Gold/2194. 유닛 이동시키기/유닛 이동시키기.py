import sys
i=sys.stdin.readline
m,n,a,b,k=map(int,i().split()) #m,a < 행 / n,b < 열
ori=[[0]*n for _ in range(m)]
for _ in range(k):
    p,q=map(int,i().split())
    p-=1;q-=1
    ori[p][q]=1

#전처리
l=[[0]*(n-b+1) for _ in range(m-a+1)]
for x in range(m-a+1):
    for y in range(n-b+1):
        l[x][y]=max(max(ori[x+i][y:y+b]) for i in range(a))
# for x in l:print(x)

        
p,q=[*map(int,i().split())]
start=(p-1,q-1)
p,q=[*map(int,i().split())]
end=(p-1,q-1)


#출발 지점에 장애물이 있으면
if l[start[0]][start[1]]==1 or l[end[0]][end[1]]==1:
    print(-1)
    exit()

#start와 end가 같으면
if start==end:print(0);exit()

visited=set()
count=0
t={start}
while q:=t:
    count+=1
    t=set()
    for x,y in q:
        visited.add((x,y))
        for d1,d2 in [[0,1],[0,-2],[1,1],[-2,0]]:
            x+=d1;y+=d2
            if 0<=x<m-a+1 and 0<=y<n-b+1 and l[x][y]==0 and (x,y) not in visited:
                if (x,y)==end:print(count);exit()
                t.add((x,y))
print(-1)
