input()
a=[0,0]
s=set()
s.add(tuple(a))
for x in input():
    if x in'EW':a[0]+='W.E'.find(x)-1
    elif x in'SN':a[1]+='S.N'.find(x)-1
    s.add(tuple(a))
print(len(s))