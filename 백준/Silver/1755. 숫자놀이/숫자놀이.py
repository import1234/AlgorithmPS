d={0:'z',1:'o',2:'tw',3:'th',4:'fo',5:'fi',6:'si',7:'se',8:'e',9:'n'}
a,b=map(int,input().split())
l=[]
for x in range(a,b+1):
    s=''
    for y in str(x):s+=d[int(y)]
    l.append((s,x))
l.sort()
i=0
for x in l:
    print(x[1],end=' ')
    i+=1
    if i%10==0:print()