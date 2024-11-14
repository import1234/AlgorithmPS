m,n=map(int,input().split())
l=[[*input()]for x in range(m)]
ans=[]
a=0
for x in range(1,m-1):
    for y in range(x+1,m):
        a=m*n
        for t in range(x):
            a-=l[t].count('W')
        for t in range(x,y):
            a-=l[t].count('B')
        for t in range(y,m):
            a-=l[t].count('R')
        ans.append(a)
print(min(ans))