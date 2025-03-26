l=[[*map(int,input().split())]for _ in' '*4]
print(sum(any(a<=x+.5<=c and b<=y+.5<=d for a,b,c,d in l)for x in range(100)for y in range(100)))