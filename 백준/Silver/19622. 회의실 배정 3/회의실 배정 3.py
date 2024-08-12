n=int(input())
l,d=[],[0,0]
for x in range(n):l.append([*map(int,input().split())][2])
for x in range(n):d.append(max(d[x]+l[x],d[x+1]))
print(d[-1])