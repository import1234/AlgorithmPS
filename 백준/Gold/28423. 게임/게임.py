result=0
g1=[10,20,30,40,50,60,70,80,90,119,1236,19135,19144]
a,b=map(int,input().split())
for x in range(a,b+1):
    ori=x
    s=set()
    while 1:
        su=0
        mu=1
        if x>100000:result-=1;break
        while x:su+=x%10;mu*=x%10;x//=10
        l=1
        while 1:
            if mu//10**l==0:break
            l+=1
        x=su*10**l+mu
        if x in s:break
        s.add(x)
        if x in g1:result+=1;break
print(result)