n=int(input())
l=[*map(int,input().split())]
t,p=map(int,input().split())
print(sum(1+(x-1)//t for x in l))
print(n//p,n%p)