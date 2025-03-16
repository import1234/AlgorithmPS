n=int(input())
s="abkdeghilmn$oprstuwy"
l=[]
for x in' '*n:
    t=''
    for x in input().replace("ng","$"):
        t+=chr(65+s.find(x))
    l.append(t)
for x in sorted(l):
    t=''
    for y in x:
        t+=s[ord(y)-65]
    print(t.replace("$","ng"))