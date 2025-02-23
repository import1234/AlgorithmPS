import sys
sys.setrecursionlimit(10000)

d={}
addr=0

for x in map(int,open(0).read().split()):
    t=0
    while t in d:
        if x<d[t]['val']:
            if d[t]['L']:
                t=d[t]['L']
            else:
                d[t]['L']=addr
                break
        else:
            if d[t]['R']:
                t=d[t]['R']
            else:
                d[t]['R']=addr
                break
    new = {'val':x, 'L':None, 'R':None}
    d[addr] = new
    addr+=1

def f(x):
    if x in d:
        f(d[x]['L'])
        f(d[x]['R'])
        print(d[x]['val'])

f(0)