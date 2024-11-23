input()
d={}
for x in map(int,input().split()):d[x]=d.get(x,0)+1
print(sum(min(d[x],2) for x in d))