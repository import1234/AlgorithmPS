for _ in ' '*int(input()):
    a,b=map(int,input().split())
    r=[f'{a//b}.'];i=0;d={}
    while i:=i+1:
        a%=b;a*=10
        if(a,b)in d:break
        d[(a,b)]=i
        r.append(f'{a//b}')
    r.insert(d[(a,b)],'(')
    print(''.join(r)+')')