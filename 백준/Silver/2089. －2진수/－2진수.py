n=int(input())
if n==0:print(0);exit()

def f(a):
    t=0
    for x in range(0,34,2):
        t+=2**x
        if t-2**x+1<=a<=t:return 2**x,x
    t=0
    for x in range(1,34,2):
        t+=2**x
        if -t<=a<=-t+2**x-1:return -2**x,x

l=[]
while n:
    t,a=f(n)
    l.append(a)
    n-=t
print(''.join('1'if x in l else'0'for x in range(l[0],-1,-1)))