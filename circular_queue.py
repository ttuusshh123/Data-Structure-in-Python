class Queue:
    def __init__(self, size):
        self.rear = -1
        self.front = -1
        self.size = size
        self.l = [None]*size

    def is_full(self):
    	return(self.front == (self.rear+1)%self.size)

    def is_empty(self):
    	return(self.front == -1)

    def enqueue(self,data):
    	if self.is_full():
    		print("Queue is full, you cannot enqueue {}".format(data))
    		print()
    	elif self.is_empty():
    		self.front = (self.front+1)%self.size
    		self.rear = (self.rear+1)%self.size
    		self.l[self.rear] = data
    	else:
    		self.rear = (self.rear+1)%self.size
    		self.l[self.rear] = data

    def dequeue(self):
    	if self.is_empty():
    		print("Queue is empty")
    		print()
    	elif self.rear == self.front:
    		temp = self.l[self.front]
    		self.front = self.rear = -1
    		return temp

    	else:
    		temp = self.l[self.front]
    		self.front = (self.front+1)%self.size
    		return temp

    def display(self):
    	if self.is_empty():
    		print("queue is EMPTY")
    	elif self.rear >= self.front:
    		for i in range(self.front, self.rear+1):
    			print(self.l[i], end = " ")
    		print()
    	elif self.front > self.rear:
    		for i in range(self.front, self.size):
    			print(self.l[i], end = " ")
    		for i in range(0, self.rear + 1):
    			print(self.l[i], end = " ")
    		print()

cq = Queue(5) 
cq.enqueue(143) 
cq.enqueue(2) 
cq.enqueue(-13) 
cq.enqueue(-6) 
cq.display() 
print("you have deleted {}".format(cq.dequeue()))
cq.display()
cq.enqueue(5)
cq.enqueue(67)
cq.display()
cq.enqueue(6)



