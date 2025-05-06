import heapq

dp=[0]*(1+10**7)
dp[0]=1
h1=[1]
h2=[1]

for x in range(10**7):
    c1=2*h1[0]+1
    c2=3*h2[0]+1
    c=min(c1,c2)
    if c1<c2:
        heapq.heappop(h1)
    elif c2<c1:
        heapq.heappop(h2)
    if c1==c2:
        heapq.heappop(h1)
        heapq.heappop(h2)
    heapq.heappush(h1,c)
    heapq.heappush(h2,c)
    dp[1+x]=c

for x in' '*int(input()):print(dp[int(input())-1])