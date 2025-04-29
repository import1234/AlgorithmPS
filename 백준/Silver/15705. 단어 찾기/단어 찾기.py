s=input()
n,m=map(int,input().split())
l=[input()for x in' '*n]

for x in range(n):
    for y in range(m):
        for a in range(-1,2):
            for b in range(-1,2):
                if a==b==0:continue
                t=0
                while 0<=x+t*a<n and 0<=y+t*b<m and l[x+t*a][y+t*b]==s[t]:
                    t+=1
                    if t==len(s):print(1);exit()
print(0)