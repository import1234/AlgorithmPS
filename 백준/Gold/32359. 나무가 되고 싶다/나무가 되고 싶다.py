from collections import deque
n=int(input())
s=set(map(int,input().split()))
q=deque([1])
c=0
while q:
    t=q.popleft()
    if t in s:continue
    c+=1
    q.append(2*t)
    q.append(2*t+1)
    if len(q)>n:print(-1);exit()
print(c)