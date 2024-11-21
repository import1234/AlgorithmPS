import sys
s,c=map(int,input().split())
l=[int(sys.stdin.readline()) for x in range(s)]

low=0
high=1000000000
while low<=high:
    mid=(low+high)//2
    if mid==0:break
    if sum(x//mid for x in l)>=c:
        low=mid+1
    else:
        high=mid-1

print(sum(l)-high*c)