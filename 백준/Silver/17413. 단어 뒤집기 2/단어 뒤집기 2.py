s=input()+' '
ans=''
p=0
t=''
while p<len(s):
    if s[p]=='<':
        ans+=t[::-1]
        t=''
        while s[p]!='>':
            t+=s[p]
            p+=1
        ans+=t+'>'
        t=''
        p+=1
        continue
    if s[p]==' ':ans+=t[::-1]+' ';t=''
    else:t+=s[p]
    p+=1
print(ans)