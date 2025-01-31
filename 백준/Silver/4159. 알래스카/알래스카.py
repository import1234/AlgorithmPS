f=lambda:int(input())
while 1:
    n=f()
    if n==0:exit()
    l=[]
    for _ in' '*n:l.append(f())
    l.sort()
    for x in l[::-1]:l.append(2*1422-x)
    if l[0]!=0:
        print('IMPOSSIBLE')
    else:
        for x in range(len(l)-1):
            if l[x+1]-l[x]>200:
                print('IM',end='')
                break
        print('POSSIBLE')