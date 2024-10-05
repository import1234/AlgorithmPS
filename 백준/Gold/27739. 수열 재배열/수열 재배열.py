n,k=map(int,input().split())
orig=[*map(int,input().split())]
result=[]
for i in range(n-k+1):
    l=orig[:]
    s=l[i:i+k]
    s.sort()
    for t in range(k):
        if k!=0:s.insert(0,s.pop())
        for j in range(k):l[i+j]=s[j]
        #print(*l)
        dp=[1]*n
        for x in range(1,n):
            if l[x]>l[x-1]:dp[x]=dp[x-1]+1
        result+=[max(dp)]
        #print(*dp)
        #print()
print(max(result))