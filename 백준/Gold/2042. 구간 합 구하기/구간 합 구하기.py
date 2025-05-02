import sys
i=sys.stdin.readline
n,m,k=map(int,i().split())
l=[int(i())for x in' '*n]
seg=[0]*4*n

def init(s,e,idx):
    if s==e:
        seg[idx]=l[s]
        l[s]=idx
        return seg[idx]
    t=(e+s)//2
    seg[idx]=init(s,t,2*idx)+init(t+1,e,2*idx+1)
    return seg[idx]

init(0,n-1,1)

for _ in' '*(m+k):
    a,b,c=map(int,i().split())
    if a==1:
        t=l[b-1]
        diff=c-seg[t]
        while t:
            seg[t]+=diff
            t//=2
    else:
        t=l[b-1]
        a=0
        while t!=1:
            if t%2==1:a+=seg[t//2]-seg[t]
            t//=2
        t=l[c-1]
        while t!=1:
            if t%2==0:a+=seg[t//2]-seg[t]
            t//=2
        print(seg[1]-a)