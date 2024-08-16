def f():
    #행 별로 구멍이 있는지 확인
    for x in range(m):
        p='.';q=0
        for y in l[x]:
            if p!=y:p=y;q+=1
        if q>2:return 0 #중간에 구멍이 있으면

def checkIfListIsHeart(r): #[5,5,2,2,2]와 같이 valid한 리스트이면 return 1
    if len(set(r))!=2 or len(r)!=max(r):return 0
    M=max(r)
    mi=min(r)
    t=M-mi
    t=[M]*(len(r)-t)+[mi]*t
    if r==t:return'd'
    elif r==t[::-1]:return'u'
    else:return 0

for _ in range(int(input())):
    m,n=map(int,input().split())
    l=[] #입력
    s=e=-1 #시작점, 끝나는점
    valid=1
    for x in range(m):
        l.append(input())
        if l[x].find('#')>=0:
            if s!=-1 and e+1!=x:valid=0 #중간에 빈 행이 있으면 0
            e=x
            if s==-1:s=x
    if valid==0 or f()==0:print(0);continue #한 행에 구멍이 있으면 0

    nl=[] #new list
    k=[]
    for x in range(m):
        t=l[x].count('#')
        if t>0:k.append(t);nl.append(l[x])
    m=len(nl)

    d=checkIfListIsHeart(k)
    if d==0:valid=0 #리스트가 valid하지 않으면 0
    elif d=='u':#[3,3,5,5,5]처럼 아래로
        length1=k[-1]
        idx1=nl[-1].find('#')
        length2=k[0]
        idx2=-1
        for x in range(1,m):
            if k[m-1-x]==length1: #큰 정사각형
                if nl[m-1-x][idx1:idx1+length1]!='#'*length1:valid=0;break
            else: #작은 정사각형
                if idx2==-1:
                    if nl[m-1-x][idx1:idx1+length2]=='#'*length2:idx2=idx1
                    elif nl[m-1-x][idx1+length1-length2:idx1+length1]=='#'*length2:idx2=idx1+length1-length2
                    else:valid=0;break
                else:
                    if nl[m-1-x][idx2:idx2+length2]!='#'*length2:valid=0;break
    else: #[5,5,5,3,3]처럼 위로
        length1=k[0]
        idx1=nl[0].find('#')
        length2=k[-1]
        idx2=-1
        for x in range(1,m):
            if k[x]==length1: #큰 정사각형
                if nl[x][idx1:idx1+length1]!='#'*length1:valid=0;break
            else: #작은 정사각형
                if idx2==-1:
                    if nl[x][idx1:idx1+length2]=='#'*length2:idx2=idx1
                    elif nl[x][idx1+length1-length2:idx1+length1]=='#'*length2:idx2=idx1+length1-length2
                    else:valid=0;break
                else:
                    if nl[x][idx2:idx2+length2]!='#'*length2:valid=0;break
    if valid==0:print(0)
    else:print(1)