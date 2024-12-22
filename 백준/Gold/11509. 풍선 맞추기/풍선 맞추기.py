n=int(input())
l=[*map(int,input().split())]
d=[0]*(max(l)+1)

c=0
for x in l:
    if d[x]>=1:
        d[x]-=1
        d[x-1]+=1
    else:
        c+=1
        d[x-1]+=1
print(c)