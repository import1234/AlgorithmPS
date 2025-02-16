f=lambda:map(int,input().split())
n,m=f()
A=[]
for x in' '*n:A.append([*f()])
m,k=f()
B=[]
for x in' '*m:B.append([*f()])
C=[[0]*k for x in' '*n]
for x in range(n):
    for y in range(k):C[x][y]=sum(A[x][z]*B[z][y]for z in range(m))
for x in C:print(*x)