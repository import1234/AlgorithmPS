import copy
inf=float('inf')
f=lambda:[*map(int,input().split())]
n=int(input())

a=f()
b=f()
d=[[inf]*3,[inf]*3,[inf]*3]

for end in range(3):
    for start in range(3):
        if end==start:continue
        d[end][start]=a[end]+b[start]

# print(d)

for _ in' '*(n-2):
    a=f()
    t=[[inf]*3,[inf]*3,[inf]*3]
    for end in range(3):
        for start in range(3):
            for mid in range(3):
                if mid==end:continue
                t[start][end]=min(t[start][end],d[start][mid]+a[end])
    d=copy.deepcopy(t)
    # print(t)

ans=inf
for x in range(3):
    for y in range(3):
        if x==y:continue
        ans=min(ans,d[x][y])
print(ans)