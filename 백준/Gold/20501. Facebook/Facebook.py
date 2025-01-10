import sys
i=sys.stdin.readline
l=[int(i(),2)for x in' '*int(i())]
for x in' '*int(i()):
    a,b=map(int,i().split())
    print((l[a-1]&l[b-1]).bit_count())