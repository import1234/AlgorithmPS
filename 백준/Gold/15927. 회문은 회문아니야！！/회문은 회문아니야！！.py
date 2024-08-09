c=lambda x:x!=x[::-1]
s=input()
if len(set(list(s)))==1:print(-1);exit()
if c(s):print(len(s))
else:print(len(s)-1)