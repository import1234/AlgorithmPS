(n,x),*l=[map(int,i.split())for i in open(0)]
print(max(s if s+t<=x else-1for s,t in l))