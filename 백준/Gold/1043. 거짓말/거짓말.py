f=lambda:map(int,input().split())
n,m=f()
people={}
for x in range(n):
    people[x+1]={'truth':0,'party':[]}
_,*l=f()
for x in l:
    people[x]['truth']=1

partyPeople={}
for x in range(m):
    _,*l=f()
    partyPeople[x+1]=l
    for y in l:people[y]['party'].append(x+1)

peopleVisited=[0]+[0]*n
partyVisited=[0]+[0]*m

ans=[0]+[1]*m
for x in range(n):
    if people[x+1]['truth'] and peopleVisited[x+1]==0:
        peopleVisited[x+1]=1
        t=set(people[x+1]['party'])
        while q:=t:
            t=set()
            for x in q: #그 사람이 갈 파티
                ans[x]=0
                for y in partyPeople[x]: #그 사람이 갈 파티에 올 사람들
                    people[y]['truth']=1
                    peopleVisited[y]=1
                    for z in people[y]['party']:
                        if partyVisited[z]==0:
                            t.add(z)
                            partyVisited[z]=1
print(sum(ans))