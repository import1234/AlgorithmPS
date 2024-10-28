n=int(input())
s=input()
l=[eval(s[2*x:2*x+3])for x in range(n//2)]
s=['+']+list(s)
for x in range(n+1):
    if s[x] not in '+*-':
        s[x]=int(s[x])

# print(s)
# print(l)
# exit()

def f(i,a):
    if i>=n+1:return a
    if i+1==n:
        if s[i]=='+':return a+s[i+1]
        elif s[i]=='*':return a*s[i+1]
        else:return a-s[i+1]
    if s[i]=='+':
        return max(f(i+2,a+s[i+1]),f(i+4,a+l[i//2]))
    elif s[i]=='*':
        return max(f(i+2,a*s[i+1]),f(i+4,a*l[i//2]))
    else:
        return max(f(i+2,a-s[i+1]),f(i+4,a-l[i//2]))

print(f(0,0))