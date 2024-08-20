for _ in range(int(input())):
    n=int(input())
    l=[[0,0],[0,0]]
    l[0].extend([*map(int,input().split())])
    l[1].extend([*map(int,input().split())])
    for x in range(n):
        l[0][2+x]+=max(l[1][1+x],l[1][x])
        l[1][2+x]+=max(l[0][1+x],l[0][x])
    print(max(l[0][-1],l[1][-1]))