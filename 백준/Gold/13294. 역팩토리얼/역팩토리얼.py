from math import log,pi
n=log(int(input()))
for x in range(1,1000000):
    if abs(x*log(x)-x-n+1/2*log(2*pi*x))<.1:
        print(x)
        exit()