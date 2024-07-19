class Queue():

    def __init__(self, list=None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def enQueue(self, i):
        self.item.append(i)

    def deQueue(self):
        return self.item.pop(0) if not self.isEmpty() else None

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []
    
    def index(self, value):
        try:
            return self.item.index(value)
        except ValueError:
            return -1

    def __str__(self):
        if not self.isEmpty():
            return str(self.item)
        else:
            return "[]"
  
p,time = input("Enter people and time : ").split(" ")
c = Queue()
c1 = Queue()
c2 = Queue()
m1 = 0
m2 = -1

for i in p:
  c.enQueue(i)

for t in range(int(time)):

    if m1 == 3:
            c1.deQueue()
            m1 = 0
    if m2 == 2:
            c2.deQueue()
            m2 = 0
    
    if c1.size() == 5 and not c.isEmpty():
            y = c.deQueue()
            c2.enQueue(y)

    if c1.size() != 5 and not c.isEmpty():
            x = c.deQueue()
            c1.enQueue(x) 

    m1 = m1 + 1
    m2 = m2 + 1
    print(t+1,end=" ")
    print(c,end=" ")
    print(c1,end=" ")
    print(c2)

# 65010536 นันทิพัฒน์ มั่งศิริ

   
