import sys
i=sys.stdin.readline
n=int(i())
l=[]
for x in' '*n:l.append(int(i(),2))
q=int(i())
for x in' '*q:
    a,b=map(int,i().split())
    a-=1;b-=1
    print((l[a]&l[b]).bit_count())