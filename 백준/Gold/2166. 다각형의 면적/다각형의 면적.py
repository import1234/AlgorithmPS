n=int(input())
ans=0
pa,pb=map(int,input().split())
fa,fb=pa,pb
for x in range(n-1):
    a,b=map(int,input().split())
    ans+=pa*b-a*pb
    pa,pb=a,b
ans+=pa*fb-fa*pb
print(abs(ans)/2)