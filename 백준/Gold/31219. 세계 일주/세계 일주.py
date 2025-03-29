n=int(input())
l=[tuple(map(int,input().split()))for x in range(n)]

q=[]
nv=set(range(n))

eps=10**-8
s=set()
def check():
    if len(q)<3:return 1
    #마지막 2점으로 직선 만들기
    [a1,b1],[a2,b2]=q[-2:]
    m1isinf=0
    if a2==a1:m1isinf=1
    else:
        m1=(b2-b1)/(a2-a1)
        f=lambda x:m1*(x-a1)+b1

    for t in range(len(q)-2):
        #직선 만들기
        [a3,b3],[a4,b4]=q[t:t+2]
        m2isinf=0
        if a3==a4:m2isinf=1
        else:
            m2=(b4-b3)/(a4-a3)
            g=lambda x:m2*(x-a3)+b3

        if m1isinf==0 and m2isinf==0:
            nu=m1*a1-m2*a3+b3-b1
            de=m1-m2
            if de==0:continue
            x=nu/de
            if min(a1,a2)+eps<x<max(a1,a2)-eps and \
                min(b1,b2)+eps<f(x)<max(b1,b2)-eps and \
                    min(a3,a4)+eps<x<max(a3,a4)-eps and \
                        min(b3,b4)+eps<g(x)<max(b3,b4)-eps:return 0
        elif m1isinf==1 and m2isinf==0:
            if min(b1,b2)+eps<g(a1)<max(b1,b2)-eps:return 0
        elif m1isinf==0 and m2isinf==1:
            if min(a1,a2)+eps<a3<max(a1,a2)-eps and \
                min(b1,b2)+eps<f(a3)<max(b1,b2)-eps:return 0
        else:
            if a1!=a3:continue
            b1,b2=min(b1,b2),max(b1,b2)
            b3,b4=min(b3,b4),max(b3,b4)
            if b1+eps<b4 and b3+eps<b2:return 0
    return 1

def addD():
    t=0
    if len(q)>=2:
        [x,y],[z,w]=q[-2:]
        t=((x-z)**2+(y-w)**2)**.5
    return t

ans=9**9
def f(st,d):
    global ans
    nv.remove(st)
    q.append(l[st])
    t=addD()
    if d+t<ans and check():
        for x in [*nv]:f(x,d+t)
        if not nv:
            q.append(q[0])
            if check():
                ans=min(ans,d+t+addD())
            q.pop()
    nv.add(st)
    q.pop()

f(0,0)
print(ans if ans!=9**9 else -1)