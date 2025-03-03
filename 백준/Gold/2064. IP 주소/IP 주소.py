l=sorted(''.join(map(lambda x:bin(int(x))[2:].zfill(8),input().split('.')))for _ in' '*int(input()))
a=[*l[0]]
f=lambda x:int(x,2)
for m in range(33):
    if m!=0:a[-m]='0'
    if f(l[-1])<=f(''.join(a))+2**m-1:break
a=''.join(a).zfill(32)
g=lambda x:f'{f(x[:8])}.{f(x[8:16])}.{f(x[16:24])}.{f(x[24:])}'
print(g(a))
print(g('1'*(32-m)+'0'*m))