h,w,c=map(int,input().split())
l=[*map(int,input().split())]
ans=[[0]*w for x in' '*h]
for x in range(w):
    for y in range(h):
        ans[y][x]=len(l)
        l[-1]-=1
        if l[-1]==0:l.pop()
for x in ans:print(''.join(map(str,x)))