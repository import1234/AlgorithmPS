a,b=' '+input().strip(),' '+input().strip()
An,Bn=len(a),len(b)
l=[[0 for x in'0'*Bn]for y in'0'*An]
for x in range(1,An):
    for y in range(1,Bn):
        if a[x]==b[y]:l[x][y]=l[x-1][y-1]+1
        else:l[x][y]=max(l[x-1][y],l[x][y-1])
print(l[-1][-1])