import heapq, sys
h=[]
for x in range(int(input())):
    q=-int(sys.stdin.readline())
    if q:heapq.heappush(h,q)
    else:
        if h:print(-heapq.heappop(h))
        else:print(0)