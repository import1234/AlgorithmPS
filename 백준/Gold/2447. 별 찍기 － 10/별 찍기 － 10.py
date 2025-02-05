def f(n):
    if n==3:return'***\n* *\n***'
    ans=''
    t=f(n//3)
    for x in t.split('\n'):ans+=x*3+'\n'
    for x in t.split('\n'):ans+=x+' '*(n//3)+x+'\n'
    for x in t.split('\n'):ans+=x*3+'\n'
    return ans[:-1]

print(f(int(input())))