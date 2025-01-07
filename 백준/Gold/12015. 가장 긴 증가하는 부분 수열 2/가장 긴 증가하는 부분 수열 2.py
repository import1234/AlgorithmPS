n=int(input())
l=[0]+[*map(int,input().split())]
dp=[0]*(n+1)
t=[0]
for x in range(1,n+1):
    s=1
    e=len(t)-1
    while s<=e:
        m=(s+e)//2
        if t[m]>=l[x]:e=m-1
        else:s=m+1
    e+=1
    if e<len(t):t[e]=min(t[e],l[x])
    else:t.append(l[x])
    dp[x]=e

# print(dp)
# print(t)

print(max(dp))