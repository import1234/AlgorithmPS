n=int(input())
A=[*map(int,input().split())]
B=[]
C=[]
c=0
t=n
s=''
while t!=0:
    if t in A:
        i=len(A)-1-A.index(t)
        for x in range(i):
            B.append(A.pop())
            s+='1 2\n'
        C.append(A.pop())
        s+='1 3\n'
        c+=i+1
    else:
        i=B.index(t)
        i=len(B)-1-B.index(t)
        for x in range(i):
            A.append(B.pop())
            s+='2 1\n'
        C.append(B.pop())
        s+='2 3\n'
        c+=i+1
    t-=1
print(c)
print(s)