n=int(input())
l=[*map(int,input().split())]
s=input()
if all(s.count(chr(97+x))<=l[x] for x in range(4)) and \
    s[-1]==s[0]=='a' and \
        all(s[x]!=s[x+1] for x in range(n-1)):print('Yes')
else:print('No')