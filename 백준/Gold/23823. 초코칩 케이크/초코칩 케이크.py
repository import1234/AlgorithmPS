import sys
i=sys.stdin.readline
n,q=map(int,i().split())

dx,dy={},{}
layerX=layerY=0
layerXlist,layerYlist=[],[]
ans=0

for x in' '*q:
    t,a=map(int,i().split())
    if t==1:
        dx[a]=dx.get(a,0)+1
        if dy=={}:
            ans=0
            if dx[a]>layerX:
                layerX=dx[a]
                layerXlist=[a]
            elif dx[a]==layerX:
                layerXlist.append(a)
            ans=len(layerXlist)*n
        else:
            ans=0
            if dx[a]>layerX:
                layerX=dx[a]
                layerXlist=[a]
            elif dx[a]==layerX:
                layerXlist.append(a)
            ans=len(layerXlist)*len(layerYlist)

    else:
        dy[a]=dy.get(a,0)+1
        if dx=={}:
            ans=0
            if dy[a]>layerY:
                layerY=dy[a]
                layerYlist=[a]
            elif dy[a]==layerY:
                layerYlist.append(a)
            ans=n*len(layerYlist)
        else:
            ans=0
            if dy[a]>layerY:
                layerY=dy[a]
                layerYlist=[a]
            elif dy[a]==layerY:
                layerYlist.append(a)
            ans=len(layerXlist)*len(layerYlist)

    print(ans)