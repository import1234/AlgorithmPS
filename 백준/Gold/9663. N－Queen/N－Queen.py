n=int(input())
l=[]
def queen(x,y):
    for a,b in l:
        if abs(x-a)==abs(y-b):return 0
    return 1

def f(x):
    global count
    for y in[*s]:
        if queen(x,y):
            if len(l)==n-1:count+=1;return
            l.append((x,y))
            s.remove(y)
            f(x+1)
            l.pop()
            s.add(y)

count=0
s={*range(n)}
f(0)
print(count)