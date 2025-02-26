while 1:
    L,R,C=map(int,input().split())
    if L+R+C==0:break
    s=(0,0,0)
    l=[]
    for x in range(L):
        l.append([])
        for y in range(R):
            l[-1].append([*input()])
            if 'S' in l[-1][-1]:
                s=(x,y,l[-1][-1].index('S'))
        input()
    
    v={s}
    t={s}
    count=0
    out=0
    while q:=t:
        count+=1
        t=set()
        for x,y,z in q:
            for a,b,c in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
                if 0<=x+a<L and 0<=y+b<R and 0<=z+c<C and l[x+a][y+b][z+c]!='#' and (x+a,y+b,z+c)not in v:
                    if l[x+a][y+b][z+c]=='E':
                        out=1
                        break
                    t.add((x+a,y+b,z+c))
                    v.add((x+a,y+b,z+c))
            if out:break
        if out:break
    if out:print(f'Escaped in {count} minute(s).')
    else:print('Trapped!')
    