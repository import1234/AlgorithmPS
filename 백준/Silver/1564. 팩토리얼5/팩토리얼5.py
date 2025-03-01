a=1
for x in range(1,int(input())+1):
    a*=x
    while a%10==0:a//=10
    a%=10**20
print(f'{a%10**5}'.zfill(5))