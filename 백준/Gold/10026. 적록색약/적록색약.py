import sys
sys.setrecursionlimit(10**5)
n=int(input())
l=''
for _ in range(n):l+=input()
k=l.replace('R','G')
def f(a):
 t=l[a];l[a]='X'
 for x in[a-n,a+n,a-1*(a%n!=0),a+1*(a%n!=n-1)]:
  if 0<=x<n*n and l[x]==t:f(x)
for t in[l,k]:
 l=list(t);c=0
 for x in range(n*n):
  if l[x]!='X':f(x);c+=1
 print(c)