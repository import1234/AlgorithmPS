for _ in ' '*int(input()):
    d={}
    a,b=map(int,input().split())
    r=[f'{a//b}.']
    a%=b
    i=1
    while 1:
        a*=10
        if (a,a//b) in d:break
        d[(a,a//b)]=i
        r.append(f'{a//b}')
        a%=b
        i+=1
    r.insert(d[(a,a//b)],'(')
    print(''.join(r)+')')