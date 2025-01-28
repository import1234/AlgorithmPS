l=[[],[],[],[]]
for x in' '*int(input()):
    for i,x in enumerate(map(int,input().split())):l[i].append(x)
d={}
for x in l[0]:
    for y in l[1]:d[x+y]=d.get(x+y,0)+1
print(sum(d.get(-x-y,0)for x in l[2]for y in l[3]))