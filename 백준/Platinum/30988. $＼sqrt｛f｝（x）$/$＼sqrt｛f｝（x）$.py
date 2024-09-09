def e():print(-1);exit()

def function_mul(l,n,r,t,p): #제곱하는 method. 곱할 리스트, 제곱할 수, 결과 리스트, 누적곱, position
    if n==0:
        r[p]+=t
        return
    for x in range(len(l)):function_mul(l,n-1,r,l[x]*t,p+x)
    return r

def function_com(a): #함수합성하는 method. 입력은 오름차순 계수
    t=len(a)-1
    r=[0]*t*t+[0]
    for x in range(t,0,-1):
        s=function_mul(a,x,[0]*t*x+[0],1,0)
        s=[0]*(t*t+1-len(s))+s
        for y in range(t*t+1):
            r[y]+=a[t-x]*s[y]
    r[-1]+=a[-1]
    return r

def check(t):
    if function_com(t)==a:
        print(m)
        print(*t)
        exit()


n=int(input())
a=[*map(int,input().split())]
if n not in[1,4,9,16,25]:e()
m=int(n**.5)


#b0 결정
B0=[]
for b0 in range(-100,101):
    if b0**(m+1)==a[0]:B0.append(b0)
if B0==[]:e()

if m==1:
    for b0 in B0:
        for b1 in range(-100,101):
            check([b0,b1])
    e()


#b1 결정
B1=[]
for b0 in B0:
    for b1 in range(-100,101):
        if b1*m*b0**m==a[1]:
            B1.append([b0,b1])
if B1==[]:e()

if m==2:
    for b0,b1 in B1:
        for b2 in range(-100,101):
            check([b0,b1,b2])
    e()


#b2 결정
B2=[]
for b0,b1 in B1:
    for b2 in range(-100,101):
        if b0*(m*(m-1)//2*b1**2*b0**(m-2)+m*b2*b0**(m-1))==a[2]:
            B2.append([b0,b1,b2])
if B2==[]:e()

if m==3:
    for b0,b1,b2 in B2:
        for b3 in range(-100,101):
            check([b0,b1,b2,b3])
    e()


#b3 결정
B3=[]
for b0,b1,b2 in B2:
    for b3 in range(-100,101):
        if m*b0**m*b3+m*(m-1)*b0**(m-1)*b1*b2+m*(m-1)*(m-2)//6*b0**(m-2)*b1**3==a[3]:
            B3.append([b0,b1,b2,b3])
if B3==[]:e()

if m==4:
    for b0,b1,b2,b3 in B3:
        for b4 in range(-100,101):
            check([b0,b1,b2,b3,b4])
    e()


#b4 결정
B4=[]
for b0,b1,b2,b3 in B3:
    for b4 in range(-100,101):
        if b0**m*b4*m+b0**(m-1)*(m*(m-1)//2*b2**2+b1*b3*m*(m-1))+b0**(m-2)*b1**2*b2*m*(m-1)//2*(m-2)+b0**(m-3)*b1**4*m*(m-1)*(m-2)*(m-3)//24==a[4]:
            B4.append([b0,b1,b2,b3,b4])
if B4==[]:e()

for b0,b1,b2,b3,b4 in B4:
    for b5 in range(-100,101):
        check([b0,b1,b2,b3,b4,b5])
e()