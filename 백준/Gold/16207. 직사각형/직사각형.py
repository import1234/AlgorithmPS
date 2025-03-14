n=int(input())
l=sorted(map(int,input().split()))
ans=0
t=[]
while l:
    t.append(l.pop())
    if len(t)<4:continue
    a,b,c,d=t
    if a==b or a-1==b:
        if c==d or c-1==d:
            ans+=b*d
            t.clear()
        else:t.remove(c)
    else:t.remove(a)
print(ans)