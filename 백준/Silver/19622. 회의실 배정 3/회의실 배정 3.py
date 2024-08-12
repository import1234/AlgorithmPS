n=int(input())
l=[]
for _ in range(n):l.append([*map(int,input().split())])
l.sort(key=lambda x:x[0])
if n<3:print(max(l[0][2],l[1*(n-1)][2]));exit()
l[2][2]+=l[0][2]
for x in range(3,n):l[x][2]+=max(l[x-2][2],l[x-3][2])
print(max(l[-x][2]for x in[1,2,3]))