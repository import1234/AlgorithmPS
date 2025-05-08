mod=10**9

def matrixMul(a,b):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%mod, (a[0][0]*b[0][1]+a[0][1]*b[1][1])%mod],
            [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%mod, (a[1][0]*b[0][1]+a[1][1]*b[1][1])%mod]]

base=[[1,1],[1,0]]

for x in' '*int(input()):
    a,b=map(int,input().split())
    ans=[[1,0],[0,1]]
    b=bin(b)[2:]
    l=[base]
    for x in range(len(b)):
        if b[len(b)-1-x]=='1':ans=matrixMul(l[x],ans)
        l.append(matrixMul(l[-1],l[-1]))
    print(a,ans[0][1])