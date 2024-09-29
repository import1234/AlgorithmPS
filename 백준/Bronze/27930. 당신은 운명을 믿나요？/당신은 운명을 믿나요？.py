s=input()
k='KOREA'
y='YONSEI'
ki=yi=0
for x in s:
    if x==k[ki]:ki+=1
    if x==y[yi]:yi+=1
    if ki==5:print(k);exit()
    if yi==6:print(y);exit()