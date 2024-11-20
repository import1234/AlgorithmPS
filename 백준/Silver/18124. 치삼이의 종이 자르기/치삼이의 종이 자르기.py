import math
n=int(input())
t=2**math.ceil(math.log2(n))
print(t-1-(t-n)//2)