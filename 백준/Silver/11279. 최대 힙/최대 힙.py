import sys
i=sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.h=[]
        self.size=0
    
    def upheap(self, n):
        self.h.append(n)
        self.size+=1
        now=self.size-1
        while now and self.h[(now-1)//2]<self.h[now]:
            self.h[(now-1)//2],self.h[now]=self.h[now],self.h[(now-1)//2]
            now=(now-1)//2
    
    def downheap(self):
        if self.size==0:print(0);return
        elif self.size==1:print(self.h.pop());self.size=0;return
        print(self.h[0])
        self.h[0]=self.h.pop()
        self.size-=1
        now=0
        while (2*now+1<self.size and self.h[now]<self.h[2*now+1]) \
        or (2*now+2<self.size and self.h[now]<self.h[2*now+2]):
            if 2*now+2>=self.size:
                self.h[now],self.h[2*now+1]=self.h[2*now+1],self.h[now]
                return
            if self.h[2*now+2]>self.h[2*now+1]:
                self.h[now],self.h[2*now+2]=self.h[2*now+2],self.h[now]
                now=2*now+2
            else:
                self.h[now],self.h[2*now+1]=self.h[2*now+1],self.h[now]
                now=2*now+1
    
    def showheap(self):
        print()
        #print(self.h)

        i=1
        for x in range(self.size):
            print(self.h[x],end=' ')
            if x+1==(1<<i)-1:print();i+=1
        print('\n')

heap=MaxHeap()
for x in '0'*int(i()):
    q=int(i())
    if q==0:heap.downheap()
    else:heap.upheap(q)
    #heap.showheap()