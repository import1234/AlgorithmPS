mod=10**6

def matrixMul(a,b):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%mod, (a[0][0]*b[0][1]+a[0][1]*b[1][1])%mod],
            [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%mod, (a[1][0]*b[0][1]+a[1][1]*b[1][1])%mod]]

a=int(input())
ans=[[1,0],[0,1]]
l=[[[1,1],[1,0]]]
t=0
while a:
    if a%2:ans=matrixMul(l[t],ans)
    l.append(matrixMul(l[-1],l[-1]))
    t+=1
    a//=2
print(ans[0][1])