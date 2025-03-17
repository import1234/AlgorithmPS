from collections import deque
for _ in range(int(input())):
    input()
    c=0
    l=deque()
    for x in input():
        x=0 if x=='H'else 1
        l.append(x)
        if l[0]==0:l.popleft()
        n=len(l)
        if n>=2 and l[-1]==l[-2]:
            l[-1]^=1
            l.popleft()
            l.popleft()
            c+=n-1
    if l:print(-1)
    else:print(c)
