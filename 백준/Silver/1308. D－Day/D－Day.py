import datetime
a1,b1,c1=map(int,input().split())
t1=datetime.datetime(a1,b1,c1,0,0,0)
a2,b2,c2=map(int,input().split())
t2=datetime.datetime(a2,b2,c2,0,0,0)
if a1+1000<=9999 and (t2-datetime.datetime(a1+1000,b1,c1,0,0,0)).days>=0:
    print('gg')
    exit()
print(f"D-{(t2-t1).days}")