def addDict(x,d):
    if x in d:d[x]+=1
    else:d[x]=1
def subDict(x,d):
    if d[x]==1:del d[x]
    else:d[x]-=1

A,T=input(),input()
avNext={} #available next letter
Ts={}
count=0
if len(T)==1:print(A.count(T));exit()
for a in A:
    if a==T[0]:
        addDict(a,Ts)
        addDict(T[1],avNext)
    elif a in avNext:
        subDict(a,avNext)
        aIdx=T.find(a)
        subDict(T[:aIdx],Ts)
        if aIdx+1==len(T):
            count+=1
        else:
            addDict(T[:aIdx+1],Ts)
            nextLetter=T[aIdx+1]
            addDict(nextLetter,avNext)
print(count)