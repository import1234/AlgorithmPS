n=int(input())
l=[[*map(int,input().split())]for x in range(n)]
if n==2:t=l[0][1]//2;print(t,t);exit()
s=[(l[0][1]-l[1][2]+l[0][2])//2]
for x in range(1,n):s+=[l[0][x]-s[0]]
print(*s)