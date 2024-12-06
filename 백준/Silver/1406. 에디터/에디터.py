import sys
i=sys.stdin.readline

class Link():
    def __init__(self):
        self.start = None
        self.cursor = None
        self.address = 0
        self.list = {-1 : {'L': None, 'R': None}} #-1: 마지막 값; eof

    def add(self, ch):
        self.address+=1
        new = {'L': None, 'R': None, 'ch': ch}

        if self.cursor == None: #list가 비어있으면
            self.start = self.cursor = self.address
            new['R'] = -1
            self.list[-1]['L'] = self.address
            self.cursor = new['R']
            self.list[self.address] = new
        
        elif self.list[self.cursor]['L'] == None: #cursor의 left가 없으면    
            new['R'] = self.cursor
            self.list[self.cursor]['L'] = self.address
            self.start = self.address
            self.cursor = new['R']
            self.list[self.address] = new
        
        else: #cursor의 left가 있으면
            prev = self.list[self.cursor]['L']
            self.list[prev]['R'] = self.address
            self.list[self.cursor]['L'] = self.address
            new['R'] = self.cursor
            new['L'] = prev
            self.cursor = new['R']
            self.list[self.address] = new
    

    def delete(self):
        if self.cursor == self.start:
            return
    
        prev = self.list[self.cursor]['L']
        if prev == self.start: #첫 문자 지우는거면
            # del self.list[prev]
            self.list[self.cursor]['L'] = None
            self.start = self.cursor
        
        else: # 중간 문자 지우는 거라면
            pprev = self.list[prev]['L']
            # del self.list[prev]
            self.list[pprev]['R'] = self.cursor
            self.list[self.cursor]['L'] = pprev



    def left(self):
        if not self.list[self.cursor]['L'] == None:
            self.cursor = self.list[self.cursor]['L']
    
    def right(self):
        if not self.list[self.cursor]['R'] == None:
            self.cursor = self.list[self.cursor]['R']
    
    def string(self):
        start = self.start
        result = ''
        while start != -1:
            result += self.list[start]['ch']
            start = self.list[start]['R']
        return result


l=Link()
for x in i().strip():l.add(x)
for x in' '*int(i()):
    s=i()
    if s[0]=='L':l.left()
    elif s[0]=='D':l.right()
    elif s[0]=='B':l.delete()
    else:l.add(s[2])
print(l.string())