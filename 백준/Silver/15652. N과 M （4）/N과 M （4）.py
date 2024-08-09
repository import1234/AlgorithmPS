n,m=map(int,input().split())
l=[]
exec('for a in range(1,n+1):\n'
     +''.join((' '*i + f'for {chr(97+i)} in range({chr(96+i)},n+1):\n') for i in range(1,m))
     +' '*m+'l=[];print('+','.join(chr(97+i) for i in range(m))+')')