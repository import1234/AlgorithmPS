l=[1,2]
while l[-1]<=10**100:l.append(l[-1]+l[-2])
while 1:
    a,b=map(int,input().split())
    if a+b==0:exit()
    print(sum(a<=x<=b for x in l))