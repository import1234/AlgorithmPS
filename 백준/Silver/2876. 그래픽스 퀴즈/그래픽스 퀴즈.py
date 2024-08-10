n=int(input())
l=[[0,0,0,0,0]]
for x in range(n):
    a,b=map(int,input().split())
    t=[0,0,0,0,0]
    for y in[a,b]:t[y-1]=l[-1][y-1]+1
    l.append(t)
M=0
i=100
for x in l:
    if M<max(x):
        M=max(x)
        i=x.index(M)+1
    elif M==max(x):
        if x.index(M)+1<i:i=x.index(M)+1
print(M,i)