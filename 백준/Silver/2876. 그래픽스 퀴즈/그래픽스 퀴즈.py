l=[[0]*6]
for x in '0'*int(input()):
    t=[0]*6
    for x in map(int,input().split()):t[x]=l[-1][x]+1
    l.append(t)
M=i=0
for x in l:
    if M<max(x):M=max(x);i=x.index(M)
    elif M==max(x) and x.index(M)<i:i=x.index(M)
print(M,i)