n=int(input())
a,b,c,f,e,d=[*map(int,input().split())]
l=[a,b,c,d,e,f]
if n==1:print(sum(l)-max(l));exit()
one=two=three=9**9
for x in range(6):
    one=min(one,l[x])
    for y in range(6):
        if x==y or (x+3)%6==y:continue
        two=min(two,l[x]+l[y])
        for z in range(6):
            if x==z or y==z or (x+3)%6==z or (y+3)%6==z:continue
            three=min(three,l[x]+l[y]+l[z])
print(one*(5*n*n-16*n+12)+two*(8*n-12)+three*4)