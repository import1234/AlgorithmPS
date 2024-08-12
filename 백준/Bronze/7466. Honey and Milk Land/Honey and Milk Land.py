import math
n,e=map(int,input().split())
t=0
if n>1:t+=sum(map(int,input().split()))**2
if n==1 and e>1:input()
if e>1:t+=sum(map(int,input().split()))**2
print(math.ceil(t**.5))