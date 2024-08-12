def r(a): #일의자리 반올림
    if a%10>=5:return a-a%10+10
    else:return a-a%10
fac=[1] #factorial
for i in range(1,200):fac.append(fac[-1]*i)

S=10**90
def sin(x, d): #수, 소수점 이하 자리수 (즉 실제 수: x/10**d)
    pi=3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825 #소수점 아래 90자리
    if x>2*pi:x-=x//(2*pi)*2*pi
    a=0
    t=x
    for n in range(0,100):
        a+=(-1)**n*t//fac[2*n+1]
        t=t*x*x//10**(d*2)
    return a

def f(x):
    return a*x+b*sin(x,90)-c*S

a,b,c=map(int,input().split())

l=0
h=10**9*S
while h-l>10000000:
    if f((l+h)//2)>=0:h=(l+h)//2+1
    else:l=(l+h)//2

print(format(r(l//10**83)/10**7,'.6f'))
