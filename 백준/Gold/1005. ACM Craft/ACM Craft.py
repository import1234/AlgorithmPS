from collections import defaultdict as dd
import sys,heapq
i=sys.stdin.readline
for _ in' '*int(i()):
    n,k=map(int,i().split())
    D=[0]+[*map(int,i().split())]
    do,di=dd(list),dd(int)
    for _ in' '*k:
        x,y=map(int,input().split())
        do[x].append(y)
        di[y]+=1
    w=int(input())

    heap=[]

    t={}
    for x in set(range(1,n+1))-di.keys():
        t[x]=0
        heapq.heappush(heap,D[x])
    T=0
    end=False
    while q:=t.copy():
        for x in q:
            if T-q[x]==D[x]:
                if x==w:
                    end=True
                    break
                del t[x]
                for y in do[x]:
                    di[y]-=1
                    if di[y]==0:
                        t[y]=T
                        heapq.heappush(heap,T+D[y])
        if end:break
        next=-1
        while next<T:
            next=heapq.heappop(heap)
        T=next
    print(T)