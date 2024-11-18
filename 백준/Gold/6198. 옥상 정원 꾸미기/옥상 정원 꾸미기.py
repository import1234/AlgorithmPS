import heapq
a=0;h=[]
for x in[*map(int,open(0).read().split())][1:]:
    while h and h[0]<=x:heapq.heappop(h)
    a+=len(h)
    heapq.heappush(h,x)
print(a)