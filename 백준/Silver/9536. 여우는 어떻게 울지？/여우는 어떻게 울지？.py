for _ in range(int(input())):
    l=input().split()
    v=set()
    while 1:
        t=input()
        if t=='what does the fox say?':
            s=[]
            for x in l:
                if x not in v:s.append(x)
            print(' '.join(s))
            break
        else:
            v.add(t.split()[2])