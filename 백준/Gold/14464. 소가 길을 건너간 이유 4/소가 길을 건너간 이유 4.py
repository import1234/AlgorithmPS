import heapq as h
c,n=map(int,input().split())
lc=sorted(int(input())for _ in' '*c)
ln=sorted([*map(int,input().split())]for _ in' '*n)
ans=p=0
pq=[]
for x in lc:
    while p<n and ln[p][0]<=x:
        h.heappush(pq,ln[p][1])
        p+=1
    while pq and not x<=pq[0]:h.heappop(pq)
    if pq:
        h.heappop(pq)
        ans+=1
print(ans)