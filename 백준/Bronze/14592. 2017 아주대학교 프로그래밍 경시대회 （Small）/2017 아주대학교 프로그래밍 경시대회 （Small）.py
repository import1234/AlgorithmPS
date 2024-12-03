n=int(input())
l=[]
for x in range(n):
    a,b,c=map(int,input().split())
    l.append((a,b,c,x+1))
    l.sort(key=lambda x:(-x[0],x[1],x[2]))
print(l[0][3])