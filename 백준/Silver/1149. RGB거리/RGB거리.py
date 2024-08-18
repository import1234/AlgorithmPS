n=int(input())
d={0:0,1:0,2:0}
for x in range(n):
    t={}
    l=[*map(int,input().split())]
    t[0]=min(d[1],d[2])+l[0]
    t[1]=min(d[0],d[2])+l[1]
    t[2]=min(d[0],d[1])+l[2]
    d=t
print(min(d.values()))