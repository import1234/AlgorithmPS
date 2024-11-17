from collections import deque
n=int(input())
if n==1:print(-1,1)
elif n==2:print(1,-1,-1,1)
else:
    dp=[deque([1,1,-1,-1,-1,1]),deque([1,1,-1,-1,1,-1,-1,1]),deque([1,1,-1,-1,1,-1,1,-1,-1,1])]
    if n<=5:print(*dp[n-3]);exit()
    for x in range(n-5):
        dp[x%3].appendleft(1)
        dp[x%3].appendleft(1)
        for y in [-1,-1,-1,1]:dp[x%3].append(y)
    print(*dp[x%3])