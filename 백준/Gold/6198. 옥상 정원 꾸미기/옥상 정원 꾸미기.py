import heapq
n=int(input())
h=[]
a=0
for x in range(n):
    t=int(input())
    while h and h[0]<=t:heapq.heappop(h)
    a+=len(h)
    heapq.heappush(h,t)
print(a)