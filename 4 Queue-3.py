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

def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

a,b = input("Enter Input : ").split("/")
X = []
Q = Queue()
A = a.split(" ")
B = b.split(",")
D = False
x = 0
for i in A :
    Q.enQueue(i)
for i in B :
    if i[0] == 'D' :
        Q.deQueue()
    if i[0] == 'E' :
        Q.enQueue(i[2:])

n = Q.size()
for j in range(n):
     x = Q.deQueue()
     X.append(int(x))

if Repeat(X) != []:
     print("Duplicate")
else:
    print("NO Duplicate")

# 65010536 นันทิพัฒน์ มั่งศิริ