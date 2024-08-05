f=lambda:map(int,input().split())
h,w=f()
n=int(*f())
l=[]
ans=[]
for x in range(n):
    a,b=f()
    l.append([a,b,a*b])
l.sort(key=lambda x:x[2],reverse=1)
for i in range(1,n):
    for j in range(i):
        [x1,x2],[y1,y2]=l[i][:2],l[j][:2]
        for a,b,c,d in [[x1,x2,y1,y2],[x2,x1,y1,y2],[x1,x2,y2,y1],[x2,x1,y2,y1]]:
            if (a<=w and b<=h and c<=w and d<=h)and(w-c>=a or h-d>=b):ans.append(a*b+c*d)
print(max(ans) if ans else 0)
