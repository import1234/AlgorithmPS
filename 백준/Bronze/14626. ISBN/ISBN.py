n=input()
for x in range(10):
    s=0
    for y in range(13):
        t=int(x if n[y]=='*'else n[y])
        s+=t*(1+2*(y%2))
    if s%10==0:print(x);exit()