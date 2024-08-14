from heapq import heappop as pop,heappush as push
import sys
i=sys.stdin.readline

for _ in'-'*int(i()):
    M,m,d=[],[],{}
    for _ in'-'*int(i()):
        a,b=i().split()
        b=int(b)
        if a=='I':
            push(M,-b)
            push(m,b)
            d[b]=1+d[b]if d.get(b)else 1
        elif d:
            if b==1:
                while M:
                    t=-pop(M)
                    if d.get(t):
                        if d[t]==1:del d[t]
                        else:d[t]-=1
                        break
            else:
                while m:
                    t=pop(m)
                    if d.get(t):
                        if d[t]==1:del d[t]
                        else:d[t]-=1
                        break
    if d:
        while t:=-M[0]:
            if d.get(t):break
            else:pop(M)
        while t:=m[0]:
            if d.get(t):break
            else:pop(m)
        print(max(d),min(d))
    else:print('EMPTY')