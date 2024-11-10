from collections import deque
d={'':'', 'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', 'b': 'd', 'd': 'b', 'i': 'i', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'q', 'q': 'p', 'r': '7', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', '0': '0', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '7': 'r', '8': '8'}
a=[*input()]
s=[]
for x in a:
    s.append('')
    s.append(x)
n=len(s)
for x in range(n):
    if s[x].upper() in d:s[x]=s[x].upper()
    if s[x].lower() in d:s[x]=s[x].lower()

ans=[]
for x in range(len(s)):
    o=s[:]
    t=deque(s)
    okay=1
    i=0
    while okay:
        if x+i<n:
            if x-i>=0:
                if o[x-i] not in d or d[o[x-i]]!=o[x+i]:okay=0;break
            else:
                if o[x+i] not in d:okay=0;break
                else:t.appendleft(d[o[x+i]])
        else:
            if x-i>=0:
                if o[x-i] not in d:okay=0;break
                else:t.append(d[o[x-i]])
            else:
                break
        i+=1
    if okay:
        ans.append(''.join(t))
if ans:
    minNum=9**9
    for x in ans:
        minNum=min(len(x),minNum)
    for x in ans:
        if len(x)==minNum:
            print(x)
            exit()
else:print(-1)