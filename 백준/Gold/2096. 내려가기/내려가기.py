n=int(input())
M=[*map(int,input().split())]
m=M[:]
for x in range(n-1):
    a,b,c=map(int,input().split())
    M=[max(M[0],M[1])+a,max(M)+b,max(M[1],M[2])+c]
    m=[min(m[0],m[1])+a,min(m)+b,min(m[1],m[2])+c]
print(max(M),min(m))