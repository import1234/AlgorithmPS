b,c,a1,a2=map(int, input().split())
l=[0,a1,a2]
for x in range(100):
    l.append(b*l[-1]+c*l[-2])
print(l[102]/l[101])