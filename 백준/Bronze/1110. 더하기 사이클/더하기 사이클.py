n=int(input())
p=n
for c in range(1000):
    a,b=p//10,p%10
    t=(a+b)%10
    p=b*10+t
    if p==n:
        print(c+1)
        exit()
print(0)