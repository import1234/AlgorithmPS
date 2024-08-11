n=int(input())
l=1
h=10**8
while l<=h:
    m=(l+h)//2
    s=0
    for x in range(1,20):s+=(5*m)//5**x
    #print(l,h,5*m,s)
    if s>n:h=m-1
    elif s<n:l=m+1
    else:print(5*m);exit()
print(-1)