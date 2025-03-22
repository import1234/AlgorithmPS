import datetime
for _ in' '*int(input()):
    l=[*map(int,input().split())]
    dt=datetime.datetime(2019,12,31,0,0,0)
    c=0
    for x in range(366):
        dt+=datetime.timedelta(days=1)
        yes=1
        for x in str(dt.month)+str(dt.day):
            if l[int(x)]==1:yes=0;break
        if yes:c+=1
    print(c)