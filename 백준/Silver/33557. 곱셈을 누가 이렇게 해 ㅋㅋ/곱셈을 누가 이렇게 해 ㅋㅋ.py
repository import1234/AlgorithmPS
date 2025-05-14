for x in' '*int(input()):
    a,b=map(int,input().split())
    t=a*b
    s=''
    while a|b:
        if a==0:s=str(b%10)+s
        elif b==0:s=str(a%10)+s
        else:s=str((a%10)*(b%10))+s
        a//=10
        b//=10
    print(1 if int(s)==t else 0)