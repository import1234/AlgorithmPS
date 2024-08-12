m=1000000007
def mul(a,b):
    r=[[0,0],[0,0]]
    for x in[0,1]:
        for y in[0,1]:
            r[x][y]=sum(a[x][z]*b[z][y] for z in[0,1])%m
    return r
M=[[[1,1],[1,0]]]
for x in range(64):M.append(mul(M[-1],M[-1]))
n=bin(int(input()))[2:][::-1]
r=[[1,0],[0,1]]
for x in range(len(n)):
    if n[x]=='1':r=mul(r,M[x])
print(r[0][1])