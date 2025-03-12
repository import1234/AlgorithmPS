from collections import defaultdict as dd
n=int(input())
l=sorted(map(int,input().split()))
if n==2:print(*sorted([0,l[0]]));exit()
if sum(l)%(n-1)!=0:print('Impossible');exit()

for x in range(2,n):
    i=l[0]+l[1]-l[x] #(a+b) + (a+c) - (b+c)
    if i%2==1:continue
    i//=2
    ans=[i]
    d=dd(int)
    for y in l:d[y]+=1
    yes=1
    for y in range(n-1):
        i=min(d)-ans[0]
        for z in ans:
            if z+i in d:
                d[z+i]-=1
                if d[z+i]==0:del d[z+i]
            else:yes=0;break
        if yes==0:break
        ans.append(i)
    if yes==0:continue
    if all(abs(x)<=10**9 for x in ans):
        print(*sorted(ans))
        exit()
print('Impossible')