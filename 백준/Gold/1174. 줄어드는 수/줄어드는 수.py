n=int(input())
if n<=10:print(n-1);exit()
l=[[*range(10)]]
c=10
for x in range(1,10):
    l.append([])
    for y in range(x,10):
        for z in l[-2]:
            if y>z//10**(x-1):
                l[-1].append(y*10**x+z)
                c+=1
                if c==n:print(l[-1][-1]);exit()
print(-1)