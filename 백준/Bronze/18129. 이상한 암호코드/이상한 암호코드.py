s,k=input().split()
k=int(k)
s=s.lower()
s+='$'
i=1
v=set()
ans=''
for x in range(len(s)-1):
    if s[x]==s[x+1]:
        i+=1
    else:
        if s[x] in v:pass
        elif i<k:ans+='0'
        else:ans+='1'
        v.add(s[x])
        i=1
print(ans)