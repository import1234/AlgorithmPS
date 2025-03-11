n=int(input())
s=input()
if n%2==1:s=s[:n//2]+s[-n//2+1:]
for x in range(26):
    if s.count(chr(97+x))%2==1:print('No');exit()
print('Yes')