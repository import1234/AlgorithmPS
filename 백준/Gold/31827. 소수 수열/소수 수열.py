primes=[]
num=[1]*1000001
for x in range(2,1001): #에라토스테네스의 체
    if num[x]==0:continue
    else:
        mul=x
        while mul*x<=1000000:
            num[mul*x]=0
            mul+=1
for x in range(2,1000001):
    if num[x]==1:primes+=[x]


n,k=map(int,input().split())
if not ((2<=n<=10000) and (2<=k<=9) and (k<=n)):
    3/0 #입력조건 테스트
V=set() #이미 사용된 소수
S=[] #슬라이딩 윈도우

#첫번째 소수쌍들 찾기
i=1000
while 1:
    if sum(primes[i:i+k])%k==0:
        for x in primes[i:i+k]:V.add(x)
        S=primes[i:i+k]
        print(*S)
        break
    i+=1

if n==k:exit()

#나머지 소수 찾기
count=0
i=1
while 1:
    if (sum(S[1:])+primes[i])%k==0 and primes[i] not in V:
        S.pop(0)
        S.append(primes[i])
        print(S[-1])
        count+=1
        if count==n-k:exit()
    i+=1