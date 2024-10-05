n,k=map(int,input().split())
orig=[*map(int,input().split())]
result=[]
for i in range(n-k+1):
    l=orig[:]
    t=sorted(l[i:i+k])
    S=[t]
    if i==0:S.append(t)
    else:
        for x in range(k):
            if t[x]>l[i-1]:break
        S.append(t[x:]+t[:x])
    if i==n-k:S.append(t)
    else:
        for x in range(k):
            if t[x]>l[i+k]:break
        S.append(t[x:]+t[:x])
    for s in S:
        for j in range(k):l[i+j]=s[j]
        c=M=1
        for x in range(1,n):
            c=c+1 if l[x]>l[x-1] else 1
            if c>M:M=c
        result+=[M]
print(max(result))