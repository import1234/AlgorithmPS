import heapq
n=int(input())
heap=[]
a=0
for x in range(n):
    t=int(input())
    if heap:
        if heap[0]<=t:
            while heap and heap[0]<=t:
                heapq.heappop(heap)
    heapq.heappush(heap,t)
    a+=len(heap)-1
print(a)