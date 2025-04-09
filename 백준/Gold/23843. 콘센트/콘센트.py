import heapq
n,m=map(int,input().split())
l=[*map(lambda x:-int(x),input().split())]
heapq.heapify(l)
a=0
while l:
    s=heapq.heappop(l)
    for x in range(m-1):
        t=0
        while l and t!=s:t+=heapq.heappop(l)
    a+=s
print(-a)