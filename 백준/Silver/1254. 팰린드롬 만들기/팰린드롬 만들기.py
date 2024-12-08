s=list(' '.join(input().strip()))
n=len(s)

a=[]
for x in range(n):
    c=0
    i=0
    if s[x]==' ':i+=1
    while 1:
        if x-i>=0 and x+i<n:
            if s[x-i]==s[x+i]:c+=2 - (x-i == x+i)
            else:break
        elif x-i>=0 and x+i>=n:
            c+=2
        elif x-i<0 and x+i<n:
            break
        else:
            a.append(c)
            break
        i+=2
print(min(a))
