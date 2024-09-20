s=0
t=-1
for x in range(int(input())):
    if x%2==0:t+=1
    s+=t
print(s)