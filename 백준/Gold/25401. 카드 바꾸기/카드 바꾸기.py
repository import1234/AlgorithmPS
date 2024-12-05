n=int(input())
l=[*map(int,input().split())]


#모든 카드 다 같은 수로 만들기
d={}
for x in l:d[x]=d.get(x,0)+1
ans=float('inf')
for x in d:ans=min(ans,n-d[x])


#등차수열 형성하기
for x in range(n):
    for y in range(x+1,n):
        a=l[y]-l[x]
        b=abs(y-x)
        if a%b!=0:continue
        a=a//b
        # print(a)
        c=0
        for i in range(n):
            # print(a*(i-x)+l[x],end=' ')
            if l[i]!=a*(i-x)+l[x]:
                c+=1
                if c>=ans:break
        # print(f'\ncount: {c}')
        ans=min(ans,c)

print(ans)