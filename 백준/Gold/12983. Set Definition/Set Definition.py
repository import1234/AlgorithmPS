from collections import deque as d

l=[1]
d1=d([1])
d2=d([1])

for _ in range(10**7):
    c1=2*d1[0]+1
    c2=3*d2[0]+1
    if c1<=c2:d1.popleft()
    if c2<=c1:d2.popleft()
    for x in[d1,d2,l]:x.append(min(c1,c2))

for x in' '*int(input()):print(l[int(input())-1])