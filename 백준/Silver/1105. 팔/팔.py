a,b=map(int,input().split())
sa,sb=str(a),str(b)
if len(sa)!=len(sb):print(0);exit()
count=0
for x in range(len(sa)):
    if sa[x]==sb[x]:
        if sa[x]=='8':count+=1
    else:break
print(count)