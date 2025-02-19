r,c=map(int,input().split())
l=[[*map(lambda x:1<<(ord(x)-65),input())]for _ in' '*r]
t,C={(0,0,l[0][0])},0
while q:=t:t={(a,b,z|l[a][b])for x,y,z in q for a,b in((x+1,y),(x-1,y),(x,y+1),(x,y-1))if r>a>=0and c>b>=0and l[a][b]&z==0};C+=1
print(C)