l=[*map(int,input().split())]
c=0
def f(i,s,t):
    global c
    if i==10:
        if s>=5:c+=1
        return
    for x in range(1,6):
        if t[0]==t[1]==x:continue
        if l[i]==x:f(i+1,s+1,[t[1],x])
        else:f(i+1,s,[t[1],x])
f(0,0,[0,0])
print(c)