from datetime import timedelta

a,b,c=map(int,input().split(':'))
dt1=timedelta(hours=a,minutes=b,seconds=c)
a,b,c=map(int,input().split(':'))
dt2=timedelta(hours=a,minutes=b,seconds=c)

if dt2<dt1:res=timedelta(days=1)+dt2-dt1
else:res=dt2-dt1
print(':'.join(x.zfill(2) for x in str(res).split(':')))