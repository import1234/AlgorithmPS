while 1:
    a,b=map(int,input().split())
    if a==b==0:break
    t={a:0};u={b:0}
    oa=a;ob=b
    c=0
    while 1:
        if a in u:
            print(f'{oa} needs {t[a]} steps, {ob} needs {u[a]} steps, they meet at {a}')
            break
        if b in t:
            print(f'{oa} needs {t[b]} steps, {ob} needs {u[b]} steps, they meet at {b}')
            break
        c+=1
        if a!=1:a=3*a+1 if a%2 else a//2
        if b!=1:b=3*b+1 if b%2 else b//2
        t[a]=min(t.get(a,9**9),c)
        u[b]=min(u.get(b,9**9),c)