n=int(input())
l=[int(a)%12*60+int(b)for _ in' '*n for a,b in[input().split(':')]]
print(min(len({(l[x]-r*x)%720for x in range(n)})for r in range(720)))