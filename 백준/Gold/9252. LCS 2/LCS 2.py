import sys
sys.setrecursionlimit(10**4)
s1=input()
s2=input()


dp={}
linked={}
lnum=0

def LCS(a,b):
    global lnum
    t=(a,b)
    if t in dp:return dp[t]

    if a<=-1 or b<=-1:
        ans=(0,lnum)
        linked[lnum]=None
        lnum+=1

    elif s1[a]==s2[b]:
        p,q=LCS(a-1,b-1)
        linked[lnum]=[s1[a],q]
        ans=(p+1,lnum)
        lnum+=1
    else:
        p0,q0=LCS(a-1,b)
        p1,q1=LCS(a,b-1)
        if p1<p0:ans=(p0,q0)
        else:ans=(p1,q1)
    
    dp[t]=ans
    return ans
    
a,b=LCS(len(s1)-1,len(s2)-1)
print(a)
t=''
def p(b):
    global t
    if linked[b]!=None:
        p(linked[b][1])
        t=''.join([t,linked[b][0]])
p(b)
print(t)