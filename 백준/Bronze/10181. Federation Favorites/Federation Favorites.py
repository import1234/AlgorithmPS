while 1:
    n=int(input())
    if n==-1:break
    l=[]
    for x in range(1,n):
        if n%x==0:l.append(x)
    if sum(l)==n:print(n,'=',' + '.join(map(str,l)))
    else:print(n,'is NOT perfect.')